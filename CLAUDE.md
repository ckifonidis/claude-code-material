# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive Claude Code guide repository structured as 13 numbered sections (01-13) covering all aspects of AI-assisted development. The project follows a specific documentation workflow with progress tracking and intelligent content processing capabilities.

### Complete Section List

1. **Introduction to AI assisted development**
2. **Getting Started with Claude Code**
3. **Important Files**
4. **Plan, Auto-accept, By-Pass**
5. **Tool usage (allow, deny)**
6. **Context Window management**
7. **Your First Application**
8. **Adding functionality to existing codebase**
9. **Documenting your codebase**
10. **Leveraging MCP to improve your workflows**
11. **Slash Commands**
12. **Subagents**
13. **Claude Code tendencies**
    - Backwards compatibility
    - Redundant additions
      - Security
      - Backwards compatibility
      - Resilience
    - Fixing the symptoms

## Key Commands

### Guide Development Workflow
```bash
# Start working on a specific guide section
/guide-workflow [section-number]

# Show all sections status
/guide-workflow

# Process content for a section (enhanced mode)
/guide-workflow [section-number] [content]
```

### Documentation Management
```bash
# Download latest Claude Code documentation
python documentation_downloader/download_docs.py --filter claude-code

# Download all Anthropic documentation
python documentation_downloader/download_docs.py

# Custom output directory
python documentation_downloader/download_docs.py --filter claude-code --output custom_docs
```

## Architecture & Structure

### Core Development Files
- **prompt.md**: Foundational project requirements and section evaluation criteria
- **PROGRESS.md**: Tracks completion status of all 13 sections with specific requirements per section
- **WORKFLOW-PROMPT.md**: Section selection and workflow management interface
- **.claude/commands/guide-workflow.md**: Enhanced slash command for intelligent content processing

### Section Structure (01-13)
Each numbered section directory follows this pattern:
- **README.md**: Core section content with standardized subsections
- **examples/**: Practical examples and code samples (when required)
- **DOS.md**: Best practices (optional, section-dependent)
- **DONTS.md**: Common mistakes (optional, section-dependent)

### Content Processing Workflow
The `/guide-workflow` command operates in three modes:
1. **Status Overview**: Display all sections and their completion status
2. **Section Selection**: Show requirements for a specific section
3. **Content Processing**: Analyze, improve, and intelligently place user-provided content

### Documentation Downloader
- Dynamically fetches URLs from https://docs.anthropic.com/llms.txt
- Downloads to `gitignore/downloaded_docs/` (ignored by git)
- Maintains directory structure matching Anthropic's documentation hierarchy
- Supports filtering by documentation sections

## Section Quality Standards

### Markdown Structure Standards
- `#` = section level (top-level guide sections)
- `##` = subsection level (within each section)
- `###` = sub-subsection level (detailed breakdowns)

### Core Requirements (Always Required)
For a section to be considered complete, the following must apply:
- **Introduction subsection**: Overview explaining purpose and scope
- **Main subsection**: Content relevant to section title (title must match section theme)
- **Official documentation references subsection**: Links to official Claude Code documentation (always the final subsection)

### Optional Requirements (Section-Dependent)
- **Examples directory**: Practical demonstrations (may not be needed for all sections)
- **DOS.md**: Best practices file (create only if relevant to section)
- **DONTS.md**: Common mistakes and warnings file (create only if relevant to section)

### Content Enhancement Process
When processing content via `/guide-workflow`, the system:
1. Analyzes content type and quality
2. Determines appropriate README subsection placement
3. Enhances formatting, clarity, and structure
4. Preserves key concepts while improving readability
5. Asks for clarification when content is ambiguous

## Development Workflow

### Section Development Process
When starting work on a section:
1. Use `/guide-workflow` or WORKFLOW-PROMPT.md to select the section to work on
2. Check PROGRESS.md for current status and specific requirements
3. Track progress as work is completed
4. Mark section complete only when all specified requirements are met

### Content Collaboration Process
When providing input for sections:
- Work collaboratively on what the input is intended for and where it should be placed
- Provide estimation and suggestion for confirmation
- User can either agree or provide alternative instructions for placement
- Content is automatically analyzed and improved before placement

### Quality Assurance
1. Content is automatically analyzed and improved before placement
2. Progress is tracked in PROGRESS.md with section-specific requirements
3. Use documentation downloader to get latest reference materials
4. Follow section evaluation criteria and markdown structure standards

## Git Workflow

- Main development in numbered section directories
- Documentation downloads go to `gitignore/` (not committed)
- Each section marked complete only when all requirements met
- Progress tracked through structured workflow system