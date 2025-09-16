# Tool Permission Management - Best Practices

This document outlines security best practices for configuring Claude Code's tool permission system.

## Security-First Configuration

### Start with Restrictive Permissions
- Begin with deny rules for sensitive operations
- Gradually allow specific tools as needed
- Use the principle of least privilege

### Essential Deny Rules
Always include these security-focused deny rules in your settings.json:

```json
{
  "permissions": {
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Read(./secrets/**)",
      "Read(./config/credentials.json)",
      "Read(~/.ssh/**)",
      "Read(~/.aws/credentials)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Bash(rm -rf:*)",
      "WebFetch"
    ]
  }
}
```

## Working with Sensitive Code

### Repository-Level Security
- Create project-specific `.claude/settings.json` files
- Check permission configurations into version control
- Review permissions regularly with your team
- Use enterprise managed policies for critical repositories

### Development Environment Isolation
- Use `additionalDirectories` sparingly and explicitly
- Consider devcontainers for additional isolation
- Regularly audit permission settings with `/permissions`
- Monitor Claude Code usage through OpenTelemetry metrics

### API Key and Secret Protection
- Always deny access to environment files and credential directories
- Use `.claude/settings.local.json` for personal sensitive configurations
- Never commit API keys or secrets to repositories
- Consider using `apiKeyHelper` scripts for dynamic credential generation

## Team Security Policies

### Permission Configuration Management
- Establish team standards for permission rules
- Use shared `.claude/settings.json` for consistent team permissions
- Document permission decisions and rationale
- Review and update permissions as projects evolve

### Onboarding New Team Members
- Provide permission configuration templates
- Train team members on security best practices
- Explain the rationale behind specific deny rules
- Set up monitoring for permission changes

### Enterprise Deployment Best Practices
- Deploy enterprise managed policies to enforce security standards
- Use SSO integration for centralized authentication
- Monitor tool usage across the organization
- Regularly audit and update security policies

## Permission Mode Strategies

### Default Mode Usage
- Use for most development scenarios
- Provides balanced security and productivity
- Allows for careful evaluation of new tool requests
- Recommended for sensitive codebases

### Accept Edits Mode Strategy
- Use only in trusted, isolated environments
- Perfect for rapid prototyping and iteration
- Still maintains security for bash commands and network operations
- Switch back to default mode for final reviews

### Plan Mode Applications
- Ideal for code reviews and analysis
- Use when you want Claude to analyze without making changes
- Perfect for understanding unfamiliar codebases
- Recommended for initial project exploration

### Bypass Permissions Mode
- **Use only in secure, isolated environments**
- Consider virtual machines or containers
- Never use with production code or sensitive data
- Implement additional monitoring when using this mode

## Monitoring and Auditing

### Regular Security Reviews
- Review permission settings monthly
- Audit tool usage logs
- Check for unauthorized permission changes
- Update security policies based on new threats

### Tool Usage Monitoring
- Enable OpenTelemetry metrics for usage tracking
- Monitor for unusual tool usage patterns
- Set up alerts for sensitive tool usage
- Regular review of permission request patterns

### Incident Response
- Have a plan for permission-related security incidents
- Know how to quickly revoke permissions
- Understand how to analyze tool usage logs
- Maintain contact information for security team

## Advanced Security Configuration

### Custom Hooks for Security
Use hooks to implement additional security checks:

```json
{
  "hooks": {
    "PreToolUse": {
      "Bash": "security-check-script.sh"
    }
  }
}
```

### Network Security
- Use `WebFetch(domain:trusted-domain.com)` for specific domains only
- Block all network tools by default
- Implement corporate proxy configurations when required
- Monitor network tool usage carefully

### File System Security
- Use absolute paths carefully: `//path/to/file` vs `/path/to/file`
- Understand the difference between project-relative and absolute paths
- Implement file access logging where required
- Regular backup of important configurations

## Compliance and Governance

### Documentation Requirements
- Document all permission decisions
- Maintain change logs for permission configurations
- Keep security review records
- Document incident response procedures

### Compliance Considerations
- Understand regulatory requirements for your industry
- Implement data protection measures
- Maintain audit trails for permission changes
- Regular compliance reviews and updates

### Risk Assessment
- Regular risk assessment of tool permissions
- Evaluate new tools for security implications
- Assess impact of permission changes
- Maintain risk register for permission-related risks