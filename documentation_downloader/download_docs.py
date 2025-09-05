#!/usr/bin/env python3
"""
Script to dynamically download Anthropic documentation files from llms.txt.
Fetches the latest documentation URLs from https://docs.anthropic.com/llms.txt
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
from typing import List, Set


def fetch_urls_from_llms_txt(filter_pattern: str = None) -> Set[str]:
    """Fetch all Anthropic docs URLs from https://docs.anthropic.com/llms.txt."""
    urls = set()
    
    # Pattern to match Anthropic docs URLs ending in .md
    pattern = r'https://docs\.anthropic\.com/[^\s\)]+\.md'
    
    try:
        print("Fetching URLs from https://docs.anthropic.com/llms.txt...")
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        
        response = requests.get('https://docs.anthropic.com/llms.txt', headers=headers, timeout=30)
        response.raise_for_status()
        
        content = response.text
        matches = re.findall(pattern, content)
        
        # Apply filter if provided
        if filter_pattern:
            filtered_matches = []
            for url in matches:
                if filter_pattern in url:
                    filtered_matches.append(url)
            matches = filtered_matches
            
        urls.update(matches)
        print(f"✓ Found {len(urls)} URLs from llms.txt")
        
    except requests.exceptions.RequestException as e:
        print(f"✗ Error fetching llms.txt: {e}")
        print("Please check your internet connection and try again.")
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
    
    return urls


def create_directory_structure(url: str, base_dir: str) -> str:
    """Create directory structure based on URL path and return full file path."""
    parsed = urlparse(url)
    
    # Remove leading slash and split path
    path_parts = parsed.path.strip('/').split('/')
    
    # Create directory structure
    dir_path = os.path.join(base_dir, *path_parts[:-1])
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
        description="Download Anthropic documentation files dynamically from llms.txt with optional filtering",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python download_docs.py                          # Download all documentation files
  python download_docs.py --filter claude-code    # Only Claude Code documentation
  python download_docs.py --filter api            # Only API documentation
  python download_docs.py --output custom_docs    # Custom output directory
        """
    )
    
    parser.add_argument(
        '--filter', '-f',
        type=str,
        help='Filter URLs containing this pattern (e.g., "claude-code", "api", "/docs/build-with-claude")'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        default="gitignore/downloaded_docs",
        help='Output directory for downloaded files'
    )
    
    args = parser.parse_args()
    
    if args.filter:
        print(f"Filtering URLs containing: '{args.filter}'")
    
    urls = fetch_urls_from_llms_txt(args.filter)
    
    print(f"Found {len(urls)} unique URLs to download")
    
    if not urls:
        print("No URLs found. Exiting.")
        return
    
    # Create base output directory
    os.makedirs(args.output, exist_ok=True)
    
    # Download each file
    successful = 0
    failed = 0
    skipped = 0
    
    for i, url in enumerate(sorted(urls), 1):
        print(f"\n[{i}/{len(urls)}]", end=" ")
        
        # Create local file path maintaining directory structure
        local_path = create_directory_structure(url, args.output)
        
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