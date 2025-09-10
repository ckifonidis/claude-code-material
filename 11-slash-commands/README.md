# Slash Commands

## Introduction
This section explains how to create and use custom slash commands in Claude Code to streamline repetitive tasks and create personalized workflows.

## Custom Command Creation and Usage

### Common Built-in Slash Commands

Claude Code provides numerous built-in slash commands for controlling behavior during interactive sessions. Here are the most commonly used ones:

#### Essential Commands
- `/help` - Get usage help and list all available commands
- `/clear` - Clear conversation history to start fresh
- `/status` - View account and system statuses
- `/cost` - Show token usage statistics

#### Configuration & Setup
- `/config` - View or modify configuration settings
- `/login` - Switch between Anthropic accounts
- `/model` - Select or change the AI model
- `/permissions` - View or update tool permissions

#### Development Workflow
- `/init` - Initialize project with CLAUDE.md guide
- `/memory` - Edit CLAUDE.md memory files
- `/review` - Request code review
- `/pr_comments` - View pull request comments

#### Advanced Features
- `/agents` - Manage custom AI subagents for specialized tasks
- `/mcp` - Manage MCP server connections and OAuth authentication
- `/compact [instructions]` - Compact conversation with optional focus instructions
- `/vim` - Enter vim mode for alternating insert and command modes

### Creating Custom Slash Commands

Custom slash commands allow you to define frequently-used prompts as Markdown files that Claude Code can execute. Commands support arguments, file references, and bash execution.

#### Command Types and Locations

**Project Commands** (shared with your team)
- Location: `.claude/commands/`
- Show as "(project)" in `/help`
- Committed to version control

**Personal Commands** (available across all projects)  
- Location: `~/.claude/commands/`
- Show as "(user)" in `/help`
- Stored in your user directory

#### Basic Command Structure

Commands are Markdown files with optional frontmatter for configuration:

```markdown
---
description: Brief description of the command
argument-hint: [expected arguments]
allowed-tools: Tool1, Tool2
model: claude-3-5-sonnet-20241022
---

Your command prompt content here.
Use $ARGUMENTS for all arguments or $1, $2, etc. for specific ones.
```

#### Argument Handling

**All Arguments**: Use `$ARGUMENTS` to capture everything
```bash
# Command: /fix-issue 123 high-priority  
# In .claude/commands/fix-issue.md:
Fix issue #$ARGUMENTS following our coding standards
# Result: Fix issue #123 high-priority following our coding standards
```

**Individual Arguments**: Use `$1`, `$2`, etc. for specific parameters
```bash
# Command: /review-pr 456 high alice
# In .claude/commands/review-pr.md:  
Review PR #$1 with priority $2 and assign to $3
# Result: Review PR #456 with priority high and assign to alice
```

#### Advanced Features

**File References**: Include file contents using `@` prefix
```markdown
Review the implementation in @src/utils/helpers.js
Compare @src/old-version.js with @src/new-version.js
```

**Bash Command Execution**: Execute commands using `!` prefix
```markdown
---
allowed-tools: Bash(git status:*), Bash(git diff:*)
---

Current status: !`git status`
Recent changes: !`git diff HEAD`
```

**Namespacing**: Organize commands in subdirectories
- `.claude/commands/frontend/component.md` → `/component (project:frontend)`
- `~/.claude/commands/security/audit.md` → `/audit (user:security)`

### MCP Slash Commands

MCP servers can expose prompts as slash commands with the pattern:
```
/mcp__<server-name>__<prompt-name> [arguments]
```

These commands are automatically discovered when MCP servers are connected and active.

## References to Official Documentation

For comprehensive information about slash commands, consult these official Claude Code documentation resources:

- **[Slash Commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)** - Complete guide to built-in and custom slash commands
- **[Common Workflows](https://docs.anthropic.com/en/docs/claude-code/common-workflows)** - File references, extended thinking, and workflow patterns
- **[Identity and Access Management](https://docs.anthropic.com/en/docs/claude-code/iam)** - Permissions system including tool-specific rules
- **[Interactive Mode](https://docs.anthropic.com/en/docs/claude-code/interactive-mode)** - Shortcuts, input modes, and interactive features
- **[MCP Integration](https://docs.anthropic.com/en/docs/claude-code/mcp)** - Model Context Protocol and MCP slash commands
- **[Settings](https://docs.anthropic.com/en/docs/claude-code/settings)** - Configuration options and command customization