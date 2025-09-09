# Claude Code Important Files

*Documentation sourced from Anthropic's official Claude Code documentation as of September 2025*

## Configuration Files

### Settings Files (`settings.json`)

Claude Code uses a hierarchical configuration system with multiple settings files:

#### User Settings
- **Location**: `~/.claude/settings.json`
- **Purpose**: Global user-wide settings
- **Scope**: Applies to all Claude Code sessions for the user

#### Project Settings
- **Shared**: `.claude/settings.json`
  - Purpose: Team-shared settings
  - Checked into version control
- **Local**: `.claude/settings.local.json`
  - Purpose: Personal project settings
  - **Not checked into version control**
  - Overrides shared project settings

#### Enterprise Managed Settings
- **macOS**: `/Library/Application Support/ClaudeCode/managed-settings.json`
- **Linux/WSL**: `/etc/claude-code/managed-settings.json`
- **Windows**: `C:\ProgramData\ClaudeCode\managed-settings.json`
- **Purpose**: Enterprise-wide policy enforcement

### Configuration Precedence (Highest to Lowest)
1. Enterprise managed policies
2. Command line arguments
3. Local project settings (`.claude/settings.local.json`)
4. Shared project settings (`.claude/settings.json`)
5. User settings (`~/.claude/settings.json`)

## Memory Management Files

### CLAUDE.md Files

Claude Code uses hierarchical memory files to provide context and instructions:

#### Enterprise Memory
- **macOS**: `/Library/Application Support/ClaudeCode/CLAUDE.md`
- **Linux**: `/etc/claude-code/CLAUDE.md`
- **Windows**: `C:\ProgramData\ClaudeCode\CLAUDE.md`

#### Project Memory
- **Location**: `./CLAUDE.md` (project root)
- **Purpose**: Project-specific context and instructions

#### User Memory
- **Location**: `~/.claude/CLAUDE.md`
- **Purpose**: Personal context and instructions

### Memory File Features
- **Hierarchical**: Higher-level files take precedence
- **Imports**: Use `@path/to/import` syntax to include other files
- **Recursive**: Supports imports up to 5 levels deep
- **Quick Add**: Use `#` shortcut to add memories
- **Editing**: Use `/memory` command to edit files

## MCP (Model Context Protocol) Files

### MCP Server Configuration
- **File**: `.mcp.json`
- **Location**: Project root directory
- **Purpose**: Configure MCP servers for the project

#### Structure Example:
```json
{
  "mcpServers": {
    "server-name": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

#### Features:
- **Environment Variables**: Supports `${VAR}` and `${VAR:-default}` expansion
- **Scopes**: local, project, user
- **Security**: Prompts for approval before using project-scoped servers

## Subagent Configuration

### Agent Files
- **User Agents**: `~/.claude/agents/`
- **Project Agents**: `.claude/agents/`
- **Format**: Markdown files with YAML frontmatter
- **Purpose**: Custom agent definitions and configurations

## Authentication Files

### Auth Configuration
- **Location**: `~/.config/claude-code/auth.json`
- **Purpose**: Stores authentication tokens and session data
- **Troubleshooting**: Delete this file to force a clean login

## Hook Configuration Files

### Hook Settings
Hooks are configured in the same settings.json files:
- `~/.claude/settings.json` (user-level)
- `.claude/settings.json` (project settings)
- `.claude/settings.local.json` (local project settings)

#### Hook Structure:
```json
{
  "hooks": {
    "PreToolUse": {
      "matcher": {
        "type": "command",
        "command": "bash command here",
        "timeout": 5000
      }
    }
  }
}
```

#### Available Hook Events:
- **PreToolUse**: Before tool call processing
- **PostToolUse**: After successful tool completion
- **UserPromptSubmit**: Before prompt processing
- **SessionStart**: When starting a new session
- **SessionEnd**: When session terminates

## Directory Structure

### Core Claude Code Directories
```
~/.claude/                    # User configuration directory
├── settings.json            # User settings
├── CLAUDE.md               # User memory file
└── agents/                 # User-defined agents

.claude/                     # Project configuration directory
├── settings.json           # Shared project settings
├── settings.local.json     # Local project settings (not committed)
└── agents/                 # Project-specific agents

~/.config/claude-code/       # System configuration
└── auth.json               # Authentication data
```

## Key Configuration Options

### Settings Categories
- **Permissions**: Tool access control
- **Environment Variables**: Custom environment setup
- **Model Selection**: Choose Claude model variants
- **Hooks**: Event-driven automation
- **Output Styles**: Customize response formatting
- **Login Methods**: Authentication preferences
- **MCP Configurations**: Model Context Protocol servers

## File Management Best Practices

### Memory Files (CLAUDE.md)
- **Be Specific**: Write clear, actionable instructions
- **Use Structure**: Organize with markdown headers
- **Regular Reviews**: Periodically update and clean up
- **Hierarchical Design**: Use imports for modular organization

### Settings Files
- **Version Control**: Commit `.claude/settings.json`, exclude `.claude/settings.local.json`
- **Security**: Never commit sensitive data like API keys
- **Documentation**: Comment complex configurations

### MCP Files
- **Security**: Review project MCP configurations before approval
- **Environment**: Use environment variables for sensitive data
- **Testing**: Validate MCP server configurations in development

## Troubleshooting Files

### Common Issues
- **Authentication**: Delete `~/.config/claude-code/auth.json` to reset
- **Configuration**: Use `/doctor` command to check installation health
- **Memory**: Check CLAUDE.md files for syntax errors
- **Permissions**: Verify settings.json permission configurations

---

*This documentation reflects the state of Claude Code as of September 2025. For the most current information, visit [https://docs.anthropic.com/en/docs/claude-code](https://docs.anthropic.com/en/docs/claude-code)*