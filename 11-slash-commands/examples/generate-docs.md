---
description: Generate comprehensive documentation for code files or modules
argument-hint: [file-path] [format: markdown|jsdoc|python-docstring]
allowed-tools: Read, Glob, Write, Bash(git log:*), Grep
---

# Documentation Generation

## Context
Target file/directory: @$1
Documentation format: $2
Recent changes: !`git log --oneline -3 -- $1`

## Your Task
Generate comprehensive documentation for @$1 in $2 format.

## Documentation Requirements

### For Functions/Methods
- Purpose and functionality description
- Parameter types and descriptions
- Return value details
- Usage examples
- Error handling information

### For Classes/Modules
- Overview and purpose
- Public API documentation
- Usage patterns and examples
- Configuration options
- Dependencies and requirements

### For APIs/Services
- Endpoint documentation
- Request/response schemas
- Authentication requirements
- Error codes and handling
- Rate limiting information

## Guidelines
- Write clear, concise descriptions
- Include practical code examples
- Document edge cases and limitations
- Follow established documentation patterns in the codebase
- Ensure examples are tested and working
- Use consistent formatting and style

## Output Format
Generate documentation in **$2** format and suggest the appropriate location for the documentation file.