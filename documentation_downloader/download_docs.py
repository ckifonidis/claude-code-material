#!/usr/bin/env python3
"""
Script to dynamically download Claude documentation files from llms.txt URLs.
Fetches the latest documentation URLs from https://docs.anthropic.com/llms.txt, https://code.claude.com/docs/llms.txt
and downloads them while maintaining proper directory structure.
Supports filtering by URL path patterns.
"""

import os
import re
import requests
import time
import argparse
from pathlib import Path
from urllib.parse import urlparse
from typing import List, Set, Dict


# Documentation source URLs
SOURCES = {
    'claude-docs': {
        'url': 'https://platform.claude.com/llms.txt',
        'pattern': r'https://platform\.claude\.com/[^\s\)]+\.md',
        'name': 'Claude Docs'
    },
    'claude-code': {
        'url': 'https://code.claude.com/docs/llms.txt',
        'pattern': r'https://[^\s\)]+\.md',
        'name': 'Claude Code Docs'
    }
}


def fetch_urls_from_source(source_name: str, source_config: Dict, filter_pattern: str = None, follow_redirects: bool = True) -> Set[tuple]:
    """Fetch documentation URLs from a source URL. Returns set of (url, source_name) tuples."""
    urls = set()

    try:
        print(f"Fetching URLs from {source_config['url']}...")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(
            source_config['url'],
            headers=headers,
            timeout=30,
            allow_redirects=follow_redirects
        )

        # Log redirects if any occurred
        if response.history:
            for resp in response.history:
                print(f"  -> Redirected from {resp.url} (HTTP {resp.status_code})")
            print(f"  -> Final URL: {response.url}")

        response.raise_for_status()

        content = response.text
        matches = re.findall(source_config['pattern'], content)

        # Apply filter if provided
        if filter_pattern:
            matches = [url for url in matches if filter_pattern in url]

        # Store as tuples of (url, source_name)
        for url in matches:
            urls.add((url, source_name))

        print(f"✓ Found {len(urls)} URLs from {source_config['name']}")

    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching {source_config['url']}: {e}")
        print("Please check your internet connection and try again.")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")

    return urls


def fetch_all_urls(sources: List[str], filter_pattern: str = None, follow_redirects: bool = True) -> Set[tuple]:
    """Fetch URLs from multiple documentation sources. Returns set of (url, source_name) tuples."""
    all_urls = set()

    for source_name in sources:
        if source_name in SOURCES:
            urls = fetch_urls_from_source(source_name, SOURCES[source_name], filter_pattern, follow_redirects)
            all_urls.update(urls)

    return all_urls


def create_directory_structure(url: str, base_dir: str, source_name: str) -> str:
    """Create directory structure based on URL path and return full file path.

    Files are organized as: base_dir/source_name/url_path
    """
    parsed = urlparse(url)

    # Remove leading slash and split path
    path_parts = parsed.path.strip('/').split('/')

    # Create directory structure with source name as parent
    dir_path = os.path.join(base_dir, source_name, *path_parts[:-1])
    os.makedirs(dir_path, exist_ok=True)

    # Return full file path
    filename = path_parts[-1]
    return os.path.join(dir_path, filename)


def download_file(url: str, local_path: str) -> bool:
    """Download a file from URL to local path."""
    try:
        print(f"Downloading: {url}")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        response = requests.get(url, headers=headers, timeout=30)
        response.raise_for_status()

        # Ensure directory exists
        os.makedirs(os.path.dirname(local_path), exist_ok=True)

        with open(local_path, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"✓ Saved: {local_path}")
        return True

    except requests.exceptions.RequestException as e:
        print(f"✗ Failed to download {url}: {e}")
        return False
    except Exception as e:
        print(f"✗ Error saving {local_path}: {e}")
        return False


def main():
    """Main function to orchestrate the download process."""
    parser = argparse.ArgumentParser(
        description="Download Claude documentation files from multiple sources with optional filtering",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python download_docs.py                              # Download from both sources
  python download_docs.py --claude-docs                # Only Claude docs (platform.claude.com)
  python download_docs.py --claude-code                # Only Claude Code docs (code.claude.com)
  python download_docs.py --filter agent-sdk           # Filter by pattern
  python download_docs.py --no-follow-redirects        # Disable redirect following
  python download_docs.py --output custom_docs         # Custom output directory
        """
    )

    parser.add_argument(
        '--filter', '-f',
        type=str,
        help='Filter URLs containing this pattern (e.g., "agent-sdk", "api", "/docs/build-with-claude")'
    )

    parser.add_argument(
        '--output', '-o',
        type=str,
        default="gitignore/downloaded_docs",
        help='Output directory for downloaded files'
    )

    parser.add_argument(
        '--claude-docs',
        action='store_true',
        help='Include Claude documentation (docs.claude.com)'
    )

    parser.add_argument(
        '--claude-code',
        action='store_true',
        help='Include Claude Code documentation (code.claude.com)'
    )

    parser.add_argument(
        '--no-follow-redirects',
        action='store_true',
        help='Disable following HTTP redirects (redirects are followed by default)'
    )

    args = parser.parse_args()

    # Determine which sources to use
    sources_to_fetch = []
    if args.claude_docs or args.claude_code:
        # User specified specific sources
        if args.claude_docs:
            sources_to_fetch.append('claude-docs')
        if args.claude_code:
            sources_to_fetch.append('claude-code')
    else:
        # Default: fetch from both sources
        sources_to_fetch = ['claude-docs', 'claude-code']

    follow_redirects = not args.no_follow_redirects

    print(f"Sources: {', '.join(sources_to_fetch)}")
    print(f"Redirect following: {'enabled' if follow_redirects else 'disabled'}")

    if args.filter:
        print(f"Filtering URLs containing: '{args.filter}'")

    url_tuples = fetch_all_urls(sources_to_fetch, args.filter, follow_redirects)

    print(f"Found {len(url_tuples)} unique URLs to download")

    if not url_tuples:
        print("No URLs found. Exiting.")
        return

    # Create base output directory
    os.makedirs(args.output, exist_ok=True)

    # Download each file
    successful = 0
    failed = 0
    skipped = 0

    for i, (url, source_name) in enumerate(sorted(url_tuples), 1):
        print(f"\n[{i}/{len(url_tuples)}]", end=" ")

        # Create local file path maintaining directory structure with source name
        local_path = create_directory_structure(url, args.output, source_name)

        # Skip if file already exists
        if os.path.exists(local_path):
            print(f"Skipping (already exists): {local_path}")
            skipped += 1
            continue

        # Download the file
        if download_file(url, local_path):
            successful += 1
        else:
            failed += 1

        # Small delay to be respectful to the server
        time.sleep(0.5)

    print(f"\n" + "="*50)
    print(f"Download complete!")
    print(f"Successfully downloaded: {successful} files")
    print(f"Skipped (already exist): {skipped} files")
    print(f"Failed downloads: {failed} files")
    print(f"Files saved to: {args.output}")


if __name__ == "__main__":
    main()