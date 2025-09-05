# Claude Code Guide

A comprehensive guide to using Claude Code for AI-assisted development, structured as a collection of focused sections covering all aspects of the development workflow.

## Quick Start

1. **New to Claude Code?** Start with [Getting Started with Claude Code](./02-getting-started-with-claude-code/)
2. **Want to contribute?** Use [WORKFLOW-PROMPT.md](./WORKFLOW-PROMPT.md) to select a section to work on
3. **Track progress:** Check [PROGRESS.md](./PROGRESS.md) for completion status

## Table of Contents

### Core Concepts
1. [Introduction to AI Assisted Development](./01-introduction-to-ai-assisted-development/) - Understanding AI-assisted development fundamentals
2. [Getting Started with Claude Code](./02-getting-started-with-claude-code/) - Installation, setup, and initial configuration
3. [Important Files](./03-important-files/) - Key configuration files and project structures

### Workflow Management
4. [Plan, Auto-accept, By-Pass](./04-plan-auto-accept-by-pass/) - Planning and execution modes
5. [Tool Usage (Allow, Deny)](./05-tool-usage-allow-deny/) - Tool permission management
6. [Context Window Management](./06-context-window-management/) - Optimizing context usage

### Practical Development
7. [Your First Application](./07-your-first-application/) - Hands-on tutorial for beginners
8. [Adding Functionality to Existing Codebase](./08-adding-functionality-to-existing-codebase/) - Extending existing projects
9. [Documenting Your Codebase](./09-documenting-your-codebase/) - Documentation strategies and automation

### Advanced Features
10. [Leveraging MCP to Improve Your Workflows](./10-leveraging-mcp-to-improve-workflows/) - Model Context Protocol integration
11. [Slash Commands](./11-slash-commands/) - Custom command creation and usage
12. [Subagents](./12-subagents/) - Specialized agent usage

### Understanding Claude Code
13. [Claude Code Tendencies](./13-claude-code-tendencies/) - Behavioral patterns and optimization strategies

## How to Use This Guide

Each section is designed to be self-contained while building upon previous concepts. Every section includes:

- **Introduction**: Overview and context
- **Main Content**: Core concepts and practical guidance
- **Examples**: Real-world scenarios and code samples (where applicable)
- **Best Practices**: DO's and DON'Ts (where applicable)
- **Official Documentation References**: Links to authoritative sources

## Documentation Downloader

This project includes a tool to automatically download the latest Anthropic documentation for offline reference:

```bash
# Download all Claude Code documentation
python documentation_downloader/download_docs.py --filter claude-code

# Download all Anthropic documentation
python documentation_downloader/download_docs.py

# Custom output directory
python documentation_downloader/download_docs.py --filter claude-code --output custom_docs
```

**Features:**
- ✅ Dynamically fetches URLs from https://docs.anthropic.com/llms.txt
- ✅ Always gets the latest documentation
- ✅ Downloads to `gitignore/downloaded_docs` (ignored by git)
- ✅ Maintains proper directory structure
- ✅ Filter by documentation sections

## Contributing

This guide is a work in progress. To contribute:

1. Review [WORKFLOW-PROMPT.md](./WORKFLOW-PROMPT.md) to select a section
2. Check [PROGRESS.md](./PROGRESS.md) for current status and requirements
3. Follow the section evaluation criteria in [prompt.md](./prompt.md)
4. Use `/guide-workflow [section-number]` command for enhanced content processing

## Project Structure

```
claude-code-guide/
├── README.md                           # This navigation file
├── WORKFLOW-PROMPT.md                  # Section selection workflow
├── PROGRESS.md                         # Completion tracking
├── .claude/commands/guide-workflow.md  # Custom slash command for development
├── documentation_downloader/
│   ├── download_docs.py               # Documentation downloader script
│   └── documentation                  # Reference documentation file
├── gitignore/                         # Ignored directory for local files
│   └── downloaded_docs/               # Downloaded documentation (auto-created)
└── [01-13]-[section-name]/            # Individual guide sections (numbered)
    ├── README.md                      # Section content
    ├── examples/                      # Practical examples
    ├── DOS.md                        # Best practices (optional)
    └── DONTS.md                      # Common mistakes (optional)
```

## Status

**Overall Progress**: 0/13 sections complete

See [PROGRESS.md](./PROGRESS.md) for detailed section-by-section status.

---

*This guide is designed to be comprehensive, practical, and continuously updated based on community needs and Claude Code evolution.*