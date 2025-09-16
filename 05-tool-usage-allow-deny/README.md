# Tool Usage (Allow, Deny)

## Introduction
This section covers Claude Code's tool permission management system, helping you understand how to control which tools Claude can access and use in your development environment.

## Tool Permission Management

Claude Code uses a sophisticated permission-based architecture that puts you in complete control of what tools Claude can access and use. This system balances the power of AI assistance with the security and safety of your development environment.

### Permission System Overview

Claude Code employs a tiered permission system designed to balance functionality with security:

| Tool Type | Example | Approval Required | Behavior |
|-----------|---------|------------------|----------|
| **Read-only** | File reads, Grep, Glob | No | Unrestricted access |
| **File Modification** | Edit, Write, MultiEdit | Yes | Requires explicit approval |
| **Bash Commands** | Shell execution | Yes | Configurable per command |
| **Network Operations** | WebFetch, WebSearch | Yes | User approval required |

### Permission Rules Configuration

You can control Claude's tool access using three types of permission rules:

#### Allow Rules
- **Purpose**: Grant automatic approval for specific tool uses
- **Behavior**: Tools run without permission prompts
- **Example**: `"Bash(npm run test)"` - Allows running npm tests automatically

#### Ask Rules
- **Purpose**: Request confirmation before tool execution
- **Behavior**: Shows permission prompt with tool details
- **Example**: `"Bash(git push:*)"` - Confirms before any git push operation

#### Deny Rules
- **Purpose**: Block specific tools or operations entirely
- **Behavior**: Prevents tool execution, no prompts shown
- **Example**: `"Read(./.env)"` - Blocks access to environment files

### Permission Modes

Claude Code supports different permission modes to match your workflow needs:

#### Default Mode (`default`)
- Standard permission behavior with prompts on first tool use
- Balanced security and usability
- Recommended for most development scenarios

#### Accept Edits Mode (`acceptEdits`)
- Auto-approves file edits and filesystem operations
- Speeds up iterative development
- Other tools still require normal permissions

#### Plan Mode (`plan`)
- Claude analyzes but cannot modify files or execute commands
- Perfect for code review and planning phases
- Read-only access only

#### Bypass Permissions Mode (`bypassPermissions`)
- **Warning**: All tools run without permission prompts
- Use only in secure, isolated environments
- Maximum speed but requires extreme caution

### Tool-Specific Permission Patterns

Different tools support specialized permission configurations:

#### Bash Commands
```json
{
  "permissions": {
    "allow": [
      "Bash(npm run build)",           // Exact command match
      "Bash(npm run test:*)",          // Prefix match with wildcard
      "Bash(git diff:*)"               // Any git diff command
    ],
    "deny": [
      "Bash(curl:*)",                  // Block all curl commands
      "Bash(rm -rf:*)"                 // Block dangerous deletions
    ]
  }
}
```

#### File Access Control
```json
{
  "permissions": {
    "allow": [
      "Read(~/Documents/*.pdf)",        // Home directory files
      "Edit(/src/**/*.ts)"             // Project TypeScript files
    ],
    "deny": [
      "Read(./.env)",                  // Environment variables
      "Read(./.env.*)",                // All env variants
      "Read(./secrets/**)",            // Secrets directory
      "Edit(//etc/**)"                 // System files (absolute path)
    ]
  }
}
```

#### Network Operations
```json
{
  "permissions": {
    "allow": [
      "WebFetch(domain:github.com)"    // Allow GitHub API calls
    ],
    "deny": [
      "WebFetch",                      // Block all web fetches
      "Bash(wget:*)",                  // Block wget downloads
      "Bash(curl:*)"                   // Block curl commands
    ]
  }
}
```

### Settings File Hierarchy

Claude Code uses a hierarchical settings system with clear precedence:

1. **Enterprise Policies** (`managed-settings.json`)
   - Cannot be overridden by users
   - Enforced across the organization
   - Located in system directories

2. **Command Line Arguments**
   - Temporary session overrides
   - Highest user-controllable precedence

3. **Local Project Settings** (`.claude/settings.local.json`)
   - Personal project preferences
   - Not shared in version control

4. **Shared Project Settings** (`.claude/settings.json`)
   - Team-shared configuration
   - Checked into source control

5. **User Global Settings** (`~/.claude/settings.json`)
   - Personal defaults across all projects

### Permission Management Commands

Use these commands to manage your permission configuration:

- **View current permissions**: `/permissions`
- **Allow a tool temporarily**: Approve when prompted and select "Yes, don't ask again"
- **Configure persistent rules**: Edit your `settings.json` file
- **Add working directories**: `/add-dir <path>` or use `additionalDirectories` setting

### Working Directory Access

By default, Claude can only access files in the directory where it was launched. You can extend this access:

- **During startup**: `claude --add-dir /path/to/additional/directory`
- **During session**: `/add-dir /path/to/additional/directory`
- **Persistent configuration**: Add to `additionalDirectories` in settings.json

### Advanced Security Features

#### Built-in Protections
- **Write access restriction**: Limited to project directories and subdirectories
- **Command injection detection**: Suspicious bash commands require manual approval
- **Network request approval**: Web operations require explicit permission
- **Prompt injection safeguards**: Context-aware analysis prevents malicious instructions

#### Enterprise Security Controls
- **Managed policy enforcement**: IT-controlled settings that cannot be overridden
- **Audit and monitoring**: Track tool usage across your organization
- **SSO integration**: Enterprise authentication with role-based access

## References to Official Documentation

For comprehensive information on Claude Code's tool permission system, consult these official documentation resources:

### Core Documentation
- **[Identity and Access Management (IAM)](https://docs.anthropic.com/en/docs/claude-code/iam)** - Complete guide to authentication, authorization, and access controls
- **[Claude Code Security](https://docs.anthropic.com/en/docs/claude-code/security)** - Security architecture, safeguards, and best practices
- **[Settings Configuration](https://docs.anthropic.com/en/docs/claude-code/settings)** - Detailed settings.json configuration options and hierarchy

### Advanced Topics
- **[SDK Permissions](https://docs.anthropic.com/en/docs/claude-code/sdk/sdk-permissions)** - Programmatic permission control for SDK implementations
- **[Hooks Guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)** - Custom permission validation using hooks
- **[Enterprise Deployment](https://docs.anthropic.com/en/docs/claude-code/iam#enterprise-managed-policy-settings)** - Managed policies and organizational controls

### Quick Reference
- **[Tool Reference](https://docs.anthropic.com/en/docs/claude-code/settings#tools-available-to-claude)** - Complete list of available tools and their permission requirements
- **[Permission Patterns](https://docs.anthropic.com/en/docs/claude-code/iam#tool-specific-permission-rules)** - Syntax and examples for tool-specific permission rules
- **[Environment Variables](https://docs.anthropic.com/en/docs/claude-code/settings#environment-variables)** - Security-related environment variables and configuration options