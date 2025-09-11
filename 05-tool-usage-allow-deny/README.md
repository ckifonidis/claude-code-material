# Tool Usage (Allow, Deny)

## Introduction

Claude Code's tool permission management system provides comprehensive control over which tools Claude can access and use in your development environment. This includes managing built-in tools, MCP server integrations, and custom subagent permissions. Understanding these controls is essential for maintaining security, optimizing workflows, and ensuring Claude operates within your intended boundaries.

## Tool Permission Management

### Understanding Tools in Claude Code

Claude Code operates through a set of powerful tools that enable it to interact with your system:

**Core Development Tools:**
- **File Operations**: Read, Write, Edit, MultiEdit for managing code files
- **Search Tools**: Grep, Glob for finding files and content
- **Shell Access**: Bash, BashOutput, KillBash for command execution
- **Web Tools**: WebSearch, WebFetch for online information access
- **Task Management**: TodoWrite, Task (subagents), ExitPlanMode
- **Notebook Support**: NotebookEdit for Jupyter notebooks

### Controlling Tool Access

#### 1. Global Tool Permissions

Configure which tools Claude can use across your entire environment:

```bash
# View current tool settings
claude settings

# Modify tool permissions in settings
claude settings set
```

Tools can be enabled or disabled in your settings configuration:
- **User-level settings**: `~/.claude/settings.json`
- **Project-level settings**: `.claude/settings.json`

#### 2. Subagent Tool Restrictions

Subagents can have limited tool access compared to the main Claude instance:

```markdown
---
name: code-reviewer
description: Reviews code for quality and security
tools: Read, Grep, Glob  # Only these tools available
---
```

Benefits of restricting subagent tools:
- **Security isolation**: Limit write access for read-only tasks
- **Focused behavior**: Prevent scope creep by limiting capabilities
- **Performance optimization**: Reduce decision complexity

#### 3. MCP Server Permissions

MCP servers extend Claude's capabilities but require careful permission management:

**Installation Scopes:**
- **Local scope**: Private to you in current project
- **Project scope**: Shared via `.mcp.json` (requires approval)
- **User scope**: Available across all your projects

```bash
# Add server with specific scope
claude mcp add --scope project shared-tool /path/to/server

# Project-scoped servers require explicit approval
claude mcp reset-project-choices  # Reset approval decisions
```

### Hook-Based Access Control

Hooks provide programmatic control over tool usage through event interception:

#### PreToolUse Hooks

Block or modify tool calls before execution:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{
          "type": "command",
          "command": "python3 check_permissions.py"
        }]
      }
    ]
  }
}
```

Example permission checker:
```python
#!/usr/bin/env python3
import json
import sys

data = json.load(sys.stdin)
file_path = data.get('tool_input', {}).get('file_path', '')

# Block edits to sensitive files
protected_paths = ['.env', 'secrets/', 'production/']
if any(p in file_path for p in protected_paths):
    print("ERROR: Cannot modify protected file")
    sys.exit(2)  # Exit code 2 blocks the tool

sys.exit(0)  # Allow the operation
```

#### PostToolUse Hooks

Audit or respond to completed tool operations:

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "echo '$(date): Command executed' >> audit.log"
        }]
      }
    ]
  }
}
```

### Security Boundaries

#### Environment Variable Protection

MCP servers and hooks can access environment variables, requiring careful management:

```bash
# Add server with specific environment variables
claude mcp add api-server --env API_KEY=value -- command

# Variables are isolated to the server process
```

#### File System Access Control

Control file system access through multiple layers:

1. **Operating system permissions**: Standard Unix permissions apply
2. **Hook-based blocking**: Programmatic access control
3. **Subagent restrictions**: Tool-level limitations
4. **MCP server isolation**: Servers run in separate processes

### Dynamic Permission Management

#### Conditional Tool Access

Implement dynamic permissions based on context:

```python
# Dynamic permission hook example
import json
import sys
import datetime

data = json.load(sys.stdin)
tool = data.get('tool')
current_hour = datetime.datetime.now().hour

# Restrict destructive operations outside business hours
if tool in ['Write', 'Edit', 'Bash'] and (current_hour < 9 or current_hour > 17):
    print("WARNING: Modifications restricted outside business hours")
    sys.exit(2)

sys.exit(0)
```

#### Permission Escalation Workflows

Create approval workflows for sensitive operations:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{
          "type": "command",
          "command": "bash -c 'read -p \"Approve command? (y/n): \" && [[ $REPLY == y ]]'"
        }]
      }
    ]
  }
}
```

### Monitoring and Auditing

#### Tool Usage Tracking

Monitor which tools Claude uses:

```bash
# Create comprehensive audit log
jq -r '"\(.timestamp) - \(.tool) - \(.tool_input)"' >> ~/.claude/tool-audit.log
```

#### MCP Server Monitoring

Track MCP server interactions:

```bash
# View MCP server status
/mcp  # Within Claude Code

# List configured servers
claude mcp list

# Check server details
claude mcp get server-name
```

### Best Practices for Tool Permissions

1. **Principle of Least Privilege**: Grant only necessary tools
2. **Defense in Depth**: Use multiple layers of access control
3. **Regular Auditing**: Review tool usage logs periodically
4. **Environment Isolation**: Separate development and production access
5. **Clear Documentation**: Document permission decisions and rationale

## References to Official Documentation

- [Claude Code Settings Guide](https://docs.anthropic.com/en/docs/claude-code/settings) - Comprehensive settings and tool configuration
- [MCP Server Integration](https://docs.anthropic.com/en/docs/claude-code/mcp) - Model Context Protocol server setup and permissions
- [Subagents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents) - Creating specialized agents with limited tools
- [Hooks Reference](https://docs.anthropic.com/en/docs/claude-code/hooks) - Event-based tool control and automation
- [Security Best Practices](https://docs.anthropic.com/en/docs/claude-code/hooks#security-considerations) - Security guidelines for hooks and permissions