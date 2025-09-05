I want to create a guide for Claude Code.
The guide will be a gihub repo and it will be structured as one directory by section.
Each section will include the README.md with the content of the section.
It can also include a DOS.md and DONTS.md for each section as needed.
It will include a directory examples that will include markdown files with examples for what is included in the content.
 
 
The readme must be separate into subsections.
The readme must include references to the official Claude Code documentation as the final subsection.
 
# means section
## means subsection
###

# Introduction to AI assisted development
# Getting Started with Claude Code
# Important Files
# Plan, Auto-accept, By-Pass
# Tool usage (allow, deny)
# Context Window management
# Your First Application
# Adding functionality to existing codebase
# Documenting your codebase
# Leveraging MCP to improve your workflows
# Slash Commands
# Subagents
# Claude Code tendencies
## Backwards compatibility
## Redundant additions
### Security
### Backwards compatibility
### Resilience
## Fixing the symptoms

 
Section evaluation
For a section to be considered complete, the following must apply:

Core Requirements (always required):
- At least a subsection introduction
- At least one main subsection. The title of the main subsection must be relevant to section title.
- At least a subsection with at least one reference to official claude code documentation

Optional Requirements (section-dependent):
- Examples under the section examples directory (may not be needed for all sections)
- DOS.md file (best practices - create only if relevant)
- DONTS.md file (common mistakes - create only if relevant)

Progress Tracking
A PROGRESS.md file will track the completion status of each section.
Each section will specify which optional requirements are needed.
The WORKFLOW-PROMPT.md will guide section selection and completion validation.

Workflow
 
When starting work on a section:
1. Use WORKFLOW-PROMPT.md to select the section to work on
2. Check PROGRESS.md for current status and requirements
3. Track progress as work is completed
4. Mark section complete only when all specified requirements are met

When you provide input:
- Work with me on what the input is intended for and where it should be placed
- Provide estimation and suggestion for confirmation
- You can either agree or provide instructions for placement