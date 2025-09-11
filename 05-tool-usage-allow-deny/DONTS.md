# Tool Usage Warnings (DON'Ts)

## Critical Security Mistakes

### DON'T: Grant Unrestricted Bash Access
```json
// DANGEROUS - No restrictions on shell commands
{
  "tools": ["Bash"]  // Can execute ANY command
}
```
**Why**: Unrestricted shell access can lead to:
- Data destruction (`rm -rf /`)
- Credential theft
- System compromise
- Unintended side effects

### DON'T: Expose Sensitive Environment Variables
```bash
# NEVER DO THIS
claude mcp add server -- env  # Exposes ALL environment variables

# ALSO AVOID
claude mcp add server --env AWS_SECRET_KEY=$AWS_SECRET_KEY
```
**Why**: Environment variables often contain:
- API keys and secrets
- Database credentials
- System configuration
- Personal information

### DON'T: Trust Unverified MCP Servers
```bash
# DANGEROUS - Installing without review
curl -s https://random-site.com/mcp-server.sh | bash
claude mcp add untrusted-server /path/to/server
```
**Why**: Malicious MCP servers can:
- Exfiltrate data
- Execute arbitrary code
- Compromise your system
- Access all available tools

### DON'T: Disable Security Hooks
```json
// NEVER remove all security checks
{
  "hooks": {}  // No protection!
}
```
**Why**: Hooks provide essential safety barriers against:
- Accidental file deletion
- Unauthorized modifications
- Dangerous command execution

## Common Permission Pitfalls

### DON'T: Use Overly Broad Tool Matchers
```json
// TOO BROAD - Catches unintended tools
{
  "matcher": ".*",  // Matches EVERYTHING
  "hooks": [...]
}
```
**Better approach**: Be specific with matchers

### DON'T: Grant Write Access to Read-Only Tasks
```markdown
---
name: log-reader
description: Reads application logs
tools: Read, Write, Edit  # Why Write and Edit for reading?
---
```
**Why**: Unnecessary permissions increase risk without benefit

### DON'T: Mix Production and Development Permissions
```bash
# DANGEROUS - Same permissions everywhere
claude mcp add --scope user production-db-access /path
```
**Why**: Production systems need stricter controls than development

### DON'T: Ignore Permission Warnings
```bash
# If you see this, STOP and investigate:
"Warning: This server requests full system access"
"Warning: Hook execution failed with error"
```
**Why**: Warnings indicate potential security issues

## Hook Implementation Mistakes

### DON'T: Use Blocking Hooks Without Feedback
```python
# BAD - No explanation why blocked
if blocked:
    sys.exit(2)  # Claude won't know why
```
**Why**: Claude needs feedback to correct behavior

### DON'T: Create Infinite Hook Loops
```json
// DANGEROUS - Hook triggers itself
{
  "PreToolUse": [{
    "matcher": "Bash",
    "hooks": [{
      "command": "bash -c 'claude ask \"Should I proceed?\"'"  // Triggers Bash hook again!
    }]
  }]
}
```
**Why**: Creates recursive loops that hang the system

### DON'T: Store Secrets in Hook Scripts
```python
# NEVER hardcode credentials
API_KEY = "sk-abc123def456"  # EXPOSED!
PASSWORD = "admin123"         # COMPROMISED!
```
**Why**: Hook scripts are often shared or version controlled

### DON'T: Use Slow Operations in Hooks
```python
# BAD - Makes every operation slow
import time
time.sleep(5)  # 5 second delay on EVERY tool use
response = requests.get("https://slow-api.com/check")
```
**Why**: Hooks run synchronously and block Claude

## MCP Server Dangers

### DON'T: Auto-Approve Project Servers
```bash
# RISKY - Bypasses security review
claude mcp reset-project-choices --auto-approve  # Not a real flag, but illustrates the danger
```
**Why**: Project servers from untrusted sources can be malicious

### DON'T: Share MCP Tokens Publicly
```json
// NEVER commit this to git
{
  "mcpServers": {
    "api": {
      "headers": {
        "Authorization": "Bearer actual-secret-token"  // EXPOSED!
      }
    }
  }
}
```
**Why**: Tokens grant access to your accounts and data

### DON'T: Run MCP Servers as Root
```bash
# DANGEROUS - Elevated privileges
sudo claude mcp add server -- command
```
**Why**: Compromised servers would have system-level access

### DON'T: Ignore MCP Output Warnings
```
"Warning: MCP tool output exceeded 10,000 tokens"
```
**Why**: Large outputs can:
- Consume context window
- Slow down processing
- Hide important information

## Subagent Misconfigurations

### DON'T: Create Overpowered Subagents
```markdown
---
name: simple-formatter
description: Formats code files
tools: Bash, Write, Edit, KillBash  # Why Bash and KillBash for formatting?
---
```
**Why**: Subagents should have minimal required tools

### DON'T: Use Vague Descriptions
```markdown
---
name: helper
description: Helps with stuff  # Too vague!
---
```
**Why**: Claude won't know when to use the subagent

### DON'T: Duplicate Tool Restrictions
```markdown
---
tools: Read, Read, Grep, Read  # Redundant
---
```
**Why**: Duplicates are confusing and serve no purpose

## Audit and Monitoring Failures

### DON'T: Ignore Audit Logs
```bash
# BAD - Never reviewing logs
~/.claude/audit.log  # 500MB and growing, never checked
```
**Why**: Logs reveal:
- Unusual activity patterns
- Failed security checks
- Potential breaches

### DON'T: Skip Permission Testing
```python
# UNTESTED hook - might block everything or nothing
def check_permission(path):
    # Complex logic never tested
    return some_complex_calculation()
```
**Why**: Untested permissions can fail catastrophically

### DON'T: Disable Logging for Performance
```json
// SHORT-SIGHTED - Sacrificing visibility
{
  "hooks": {
    "PostToolUse": []  // Removed logging "for speed"
  }
}
```
**Why**: You lose ability to debug issues and detect problems

## Integration Anti-Patterns

### DON'T: Mix Personal and Work Configurations
```bash
# RISKY - Work settings in personal config
~/.claude/settings.json  # Contains work API keys
```
**Why**: Accidental exposure of work resources

### DON'T: Use Production Credentials in Development
```bash
# DANGEROUS
export PROD_DB_PASSWORD="real-password"
claude mcp add dev-server --env PROD_DB_PASSWORD=$PROD_DB_PASSWORD
```
**Why**: Development environments are less secure

### DON'T: Skip Version Control for Security Configs
```bash
# BAD - No tracking of changes
.gitignore:
.claude/  # Ignoring ALL Claude configs
```
**Why**: Can't track security changes or roll back

## Performance and Stability Risks

### DON'T: Create Complex Hook Chains
```json
// FRAGILE - Too many dependencies
{
  "hooks": [{
    "command": "script1.sh | script2.py | script3.js | script4.rb"
  }]
}
```
**Why**: Any script failure breaks the entire chain

### DON'T: Use Unreliable External Services in Hooks
```python
# RISKY - External dependency
response = requests.get("https://unreliable-api.com/check")
if response.status_code != 200:
    sys.exit(2)  # Blocks Claude when API is down
```
**Why**: External failures shouldn't break local development

### DON'T: Implement Stateful Hooks
```python
# BAD - Maintains state between calls
global counter
counter += 1
if counter > 10:
    block_everything()  # Unexpected behavior
```
**Why**: Hooks should be stateless and predictable

## Recovery and Rollback Mistakes

### DON'T: Make Irreversible Permission Changes
```bash
# NO BACKUP - Can't undo
rm ~/.claude/settings.json.backup
echo "{}" > ~/.claude/settings.json
```
**Why**: Need ability to restore working configuration

### DON'T: Test Security Changes in Production
```bash
# RECKLESS - Testing on live system
claude mcp add experimental-security-tool -- /untested/script
```
**Why**: Test in isolated environments first

### DON'T: Ignore Error Messages
```
"Error: Hook script not found"
"Error: Permission denied"
"Error: Invalid tool configuration"
```
**Why**: Errors indicate broken security controls

## Remember

**Security is not optional** - These warnings exist because real incidents have occurred. Always:
- Review before trusting
- Test before deploying  
- Monitor after implementing
- Document for others

When in doubt, choose the more restrictive option and expand permissions only when necessary.