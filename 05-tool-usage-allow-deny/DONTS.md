# Tool Permission Management - Common Mistakes and Security Warnings

This document outlines common mistakes and security pitfalls to avoid when configuring Claude Code's tool permission system.

## Critical Security Warnings

### ⚠️ NEVER Use Bypass Permissions Mode in Production
**DON'T:**
```json
{
  "permissions": {
    "defaultMode": "bypassPermissions"
  }
}
```

**Why this is dangerous:**
- Claude gets unrestricted access to your entire system
- No protection against malicious commands or prompt injection
- Can accidentally delete files, expose secrets, or modify critical systems
- Bypasses all security safeguards

**Instead:**
- Use `bypassPermissions` only in isolated test environments
- Prefer `acceptEdits` mode for faster iteration with maintained security
- Always return to `default` mode for production work

### ⚠️ NEVER Allow Unrestricted Network Access
**DON'T:**
```json
{
  "permissions": {
    "allow": [
      "Bash(curl:*)",
      "Bash(wget:*)",
      "WebFetch"
    ]
  }
}
```

**Why this is dangerous:**
- Enables data exfiltration attacks
- Allows downloading and executing malicious scripts
- Bypasses corporate firewall and security policies
- Can expose internal network information

## Bash Permission Pattern Pitfalls

### ❌ Common Bash Pattern Bypass Scenarios

**Problem:** Thinking prefix patterns are secure
```json
{
  "permissions": {
    "allow": ["Bash(curl http://github.com/:*)"]
  }
}
```

**Easily bypassed by:**
- Options before URL: `curl -X GET http://github.com/malicious`
- Different protocol: `curl https://github.com/malicious`
- Variables: `URL=http://github.com/bad && curl $URL`
- Redirects: `curl -L http://bit.ly/malicious` (redirects to anywhere)
- Extra spaces: `curl  http://github.com/malicious`

**Better approach:**
- Use WebFetch with domain restrictions: `WebFetch(domain:github.com)`
- Implement custom hooks for complex validation
- Use comprehensive deny rules rather than overly specific allow rules

### ❌ Wildcard Misunderstanding
**DON'T:**
```json
{
  "permissions": {
    "allow": ["Bash(git *)", "Bash(npm *)"]
  }
}
```

**Why this fails:**
- Wildcards only work at the end with `:*` syntax
- This pattern won't match anything
- Creates false sense of security

**Correct syntax:**
```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)"
    ]
  }
}
```

## File Path Configuration Mistakes

### ❌ Absolute Path Confusion
**DON'T:**
```json
{
  "permissions": {
    "deny": ["/Users/alice/secrets/**"]
  }
}
```

**Why this fails:**
- `/path` is relative to your settings file, NOT an absolute path
- This actually blocks `<settings-location>/Users/alice/secrets/`
- Real secrets remain accessible

**Correct absolute path:**
```json
{
  "permissions": {
    "deny": ["//Users/alice/secrets/**"]
  }
}
```

### ❌ Incomplete Secret Protection
**DON'T:**
```json
{
  "permissions": {
    "deny": [".env"]
  }
}
```

**Missing variations:**
- `.env.local`, `.env.production`, `.env.development`
- `config/secrets.json`, `secrets/`, `.aws/credentials`
- SSH keys, API keys in various locations

**Comprehensive protection:**
```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/credentials)"
    ]
  }
}
```

## Permission Hierarchy Misunderstandings

### ❌ Assuming Local Settings Override Everything
**DON'T:** Rely on local settings to override enterprise policies

**Reality:**
1. Enterprise managed policies (cannot be overridden)
2. Command line arguments
3. Local project settings
4. Shared project settings
5. User settings

**Remember:** Enterprise policies always win, regardless of your local configuration.

### ❌ Forgetting Settings Precedence
**DON'T:** Configure permissions only in user settings for team projects

**Problems:**
- Team members may have different permission configurations
- Local project settings can override your user defaults
- Shared project settings should define team standards

## MCP Security Mistakes

### ❌ Incorrect MCP Wildcard Usage
**DON'T:**
```json
{
  "permissions": {
    "allow": ["mcp__github__*"]
  }
}
```

**Why this fails:**
- MCP permissions don't support wildcards
- This rule won't match any MCP tools
- Creates security gaps

**Correct MCP permissions:**
```json
{
  "permissions": {
    "allow": [
      "mcp__github",                    // All GitHub tools
      "mcp__github__get_issue",         // Specific tool only
      "mcp__github__list_issues"        // Another specific tool
    ]
  }
}
```

## Configuration Management Anti-Patterns

### ❌ Hardcoding Personal Paths in Shared Settings
**DON'T:**
```json
{
  "permissions": {
    "additionalDirectories": [
      "/Users/alice/my-personal-projects"
    ]
  }
}
```

**Problems:**
- Breaks for other team members
- Exposes personal directory structure
- Should be in `.claude/settings.local.json` instead

### ❌ Overly Permissive Default Configurations
**DON'T:**
```json
{
  "permissions": {
    "allow": [
      "Bash",
      "WebFetch",
      "Edit"
    ],
    "defaultMode": "acceptEdits"
  }
}
```

**Security issues:**
- Allows all bash commands without restriction
- Permits unrestricted web access
- Auto-approves all file edits
- Essentially disables security system

## Monitoring and Auditing Mistakes

### ❌ Not Monitoring Permission Changes
**Common oversight:**
- No tracking of who changed permissions when
- No alerts for sensitive permission grants
- No regular audits of permission configurations

**Impact:**
- Security breaches go undetected
- Cannot trace permission-related incidents
- No compliance audit trail

### ❌ Ignoring Tool Usage Patterns
**Warning signs to watch for:**
- Unusual network tool usage
- Unexpected file access patterns
- High-privilege tool usage spikes
- Failed permission requests

## Team Collaboration Pitfalls

### ❌ Not Documenting Permission Decisions
**Problems:**
- Team members don't understand why certain rules exist
- Makes it difficult to modify permissions safely later
- No context for future security reviews

### ❌ Inconsistent Permission Policies Across Projects
**Issues:**
- Different security levels for similar projects
- Team confusion about standards
- Harder to maintain and audit

### ❌ Not Training Team Members
**Consequences:**
- Accidental security misconfigurations
- Reduced effectiveness of security measures
- Increased risk of human error

## Recovery and Incident Response Mistakes

### ❌ No Permission Rollback Plan
**What can go wrong:**
- Accidentally granting overly broad permissions
- No way to quickly revert to safe configuration
- Extended exposure during incident response

### ❌ Not Having Emergency Access Procedures
**Critical oversight:**
- No way to quickly revoke permissions during security incident
- No escalation procedures for permission-related emergencies
- No contact information for security team

## Best Practices Summary

**Always:**
- Start with restrictive permissions and gradually allow specific tools
- Use the principle of least privilege
- Document all permission decisions
- Regularly audit and review configurations
- Monitor tool usage patterns
- Train team members on security practices

**Never:**
- Use `bypassPermissions` mode in production
- Allow unrestricted network access
- Ignore bash pattern limitations
- Hardcode personal paths in shared settings
- Skip monitoring and auditing
- Assume local settings can override enterprise policies