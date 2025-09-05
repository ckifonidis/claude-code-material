---
allowed-tools: Bash(find:*), Bash(ls:*), Bash(wc:*), Bash(head:*), Read, Write, Glob
argument-hint: [target-path] [--exclude pattern]
description: Generate CLAUDE.md files for repository documentation
---

# Repository Documentation Generator

## Current Repository Structure
!`find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.cs" -o -name "*.java" -o -name "*.go" -o -name "*.rs" -o -name "package.json" -o -name "*.config.js" -o -name "appsettings.json" -o -name "Dockerfile" -o -name "*.yml" -o -name "*.yaml" \) | grep -v -E "(node_modules|\.git|bin|obj|target|dist|build|\.venv|__pycache__|\.next)" | head -50`

## Target Directories for Documentation
!`find ${1:-.} -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.cs" -o -name "*.java" -o -name "*.go" -o -name "*.rs" -o -name "package.json" -o -name "*.config.js" -o -name "appsettings.json" -o -name "Dockerfile" -o -name "*.yml" -o -name "*.yaml" \) | grep -v -E "(node_modules|\.git|bin|obj|target|dist|build|\.venv|__pycache__|\.next)" | xargs dirname | sort -u`

## Your Task

Generate CLAUDE.md files for each target directory above. For each directory:

1. **Analyze the directory contents** - Look at file types, naming patterns, and structure
2. **Determine the purpose** - What does this directory/module do in the larger system?
3. **Identify key files** - Which files are most important and what do they do?
4. **Map dependencies** - Internal dependencies (other directories) and external ones (from package files)
5. **Document usage patterns** - How do other parts of the system interact with this?
6. **Note architecture** - Any design patterns, conventions, or architectural decisions

## CLAUDE.md Template Structure

For each directory, create a CLAUDE.md file with this structure:

```markdown
# [Directory Name]

## Purpose
[1-2 sentence description of what this directory/module does]

## Key Files
- **filename.ext**: [Brief description of purpose and functionality]
- **config.json**: [What this configures and key settings]

## Dependencies
### Internal
- ../other/module (for shared utilities)
- ../core/types (for type definitions)

### External
- package-name@version (purpose in this module)

## Usage
[How other parts of the codebase interact with this module]

## Architecture Notes
[Design patterns, conventions, architectural decisions used here]
```

## Process Instructions

1. Start with leaf directories (those with no subdirectories containing code)
2. Work your way up to parent directories
3. Skip directories that already have CLAUDE.md files unless they need updates
4. Focus on directories with substantive code/config, not just build artifacts
5. Keep descriptions concise but informative for LLM context

Begin generating documentation for the target directories identified above.