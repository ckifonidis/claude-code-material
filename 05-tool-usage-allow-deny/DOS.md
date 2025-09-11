# Tool Usage Best Practices (DOs)

## Security Best Practices

### DO: Apply Principle of Least Privilege
- Start with minimal tool access and expand as needed
- Grant only the tools necessary for specific tasks
- Regularly review and revoke unnecessary permissions

### DO: Use Layered Security
- Combine multiple access control methods:
  - Operating system permissions
  - Hook-based controls
  - Subagent restrictions
  - MCP server isolation

### DO: Implement Audit Logging
```bash
# Create comprehensive audit trail
jq -r '"[\(.timestamp)] \(.tool) - \(.tool_input.file_path // .tool_input.command // "N/A")"' >> ~/.claude/audit.log
```

### DO: Protect Sensitive Files
```python
# Use PreToolUse hooks to protect critical files
protected_files = ['.env', 'secrets.json', 'private.key']
if file_path in protected_files:
    sys.exit(2)  # Block the operation
```

## Subagent Tool Management

### DO: Create Focused Subagents
```markdown
---
name: documentation-writer
description: Creates and updates documentation
tools: Read, Write, Grep  # Only documentation-related tools
---
```

### DO: Isolate Risky Operations
- Create separate subagents for:
  - Database operations
  - Production deployments
  - System configuration changes
  - External API interactions

### DO: Document Tool Rationale
```markdown
---
name: code-analyzer
description: Analyzes code quality and patterns
tools: Read, Grep, Glob  # Read-only access for safety
# Rationale: Analysis only, no modifications needed
---
```

## MCP Server Configuration

### DO: Use Appropriate Scopes
```bash
# Personal tools: user scope
claude mcp add --scope user personal-tool /path

# Team tools: project scope
claude mcp add --scope project team-tool /path

# Temporary tools: local scope (default)
claude mcp add temp-tool /path
```

### DO: Validate MCP Servers
- Review server source code before installation
- Test servers in isolated environments first
- Monitor server behavior with hooks

### DO: Manage Environment Variables Carefully
```bash
# Provide only necessary environment variables
claude mcp add api-client --env API_KEY=$API_KEY -- command

# Never expose sensitive system variables
```

## Hook Implementation

### DO: Create Informative Hook Messages
```python
# Provide clear feedback to Claude
if error_condition:
    print("ERROR: Cannot modify production database during peak hours")
    print("SUGGESTION: Schedule this operation after 6 PM")
    sys.exit(2)
```

### DO: Use Exit Codes Appropriately
- `0`: Allow operation to proceed
- `2`: Block operation and provide feedback
- Other codes: System-specific handling

### DO: Make Hooks Efficient
```python
# Cache expensive operations
import pickle
import os

CACHE_FILE = '/tmp/hook_cache.pkl'

if os.path.exists(CACHE_FILE):
    with open(CACHE_FILE, 'rb') as f:
        data = pickle.load(f)
else:
    data = expensive_operation()
    with open(CACHE_FILE, 'wb') as f:
        pickle.dump(data, f)
```

## Permission Workflows

### DO: Implement Approval Mechanisms
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Bash",
      "hooks": [{
        "type": "command",
        "command": "bash -c 'echo \"Command: $(jq -r .tool_input.command)\" && read -p \"Approve? (y/n): \" && [[ $REPLY == y ]]'"
      }]
    }]
  }
}
```

### DO: Create Time-Based Restrictions
```python
# Limit certain operations to business hours
import datetime

now = datetime.datetime.now()
if now.weekday() >= 5:  # Weekend
    print("Operations restricted on weekends")
    sys.exit(2)
```

### DO: Use Context-Aware Permissions
```python
# Check git branch before allowing modifications
import subprocess

branch = subprocess.check_output(['git', 'branch', '--show-current']).decode().strip()
if branch == 'main' and tool in ['Write', 'Edit']:
    print("Direct edits to main branch not allowed")
    sys.exit(2)
```

## Monitoring and Compliance

### DO: Regular Permission Audits
```bash
# Weekly review script
#!/bin/bash
echo "=== Tool Usage Report ==="
echo "This week's most used tools:"
cat ~/.claude/audit.log | grep "$(date -d '7 days ago' +%Y-%m-%d)" | cut -d' ' -f3 | sort | uniq -c | sort -rn
```

### DO: Track MCP Server Usage
```bash
# Monitor active MCP connections
claude mcp list | tee mcp_inventory.txt

# Check for unauthorized servers periodically
diff mcp_inventory.txt approved_servers.txt
```

### DO: Document Security Decisions
Create a `SECURITY.md` file documenting:
- Why certain tools are restricted
- Rationale for hook implementations
- MCP server approval criteria
- Incident response procedures

## Testing and Validation

### DO: Test Hooks Thoroughly
```bash
# Test hook with sample input
echo '{"tool": "Edit", "tool_input": {"file_path": "test.txt"}}' | python3 permission_hook.py
```

### DO: Validate Permission Changes
- Test in development environment first
- Use version control for hook scripts
- Document expected vs actual behavior

### DO: Create Permission Test Suites
```python
# test_permissions.py
test_cases = [
    {"tool": "Write", "path": "/etc/passwd", "expected": "block"},
    {"tool": "Read", "path": "README.md", "expected": "allow"},
    {"tool": "Bash", "command": "rm -rf /", "expected": "block"}
]

for case in test_cases:
    result = test_permission(case)
    assert result == case["expected"]
```

## Performance Optimization

### DO: Cache Permission Decisions
```python
# Cache frequently checked permissions
from functools import lru_cache

@lru_cache(maxsize=100)
def check_file_permission(file_path):
    # Expensive permission check
    return is_allowed(file_path)
```

### DO: Use Efficient Matchers
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Edit|Write|MultiEdit",  // Single regex for multiple tools
      "hooks": [{"type": "command", "command": "check_write.py"}]
    }]
  }
}
```

### DO: Minimize Hook Overhead
- Avoid network calls in hooks when possible
- Use lightweight scripting languages
- Exit early for non-matching conditions

## Integration Best Practices

### DO: Coordinate with CI/CD
```yaml
# .github/workflows/validate-hooks.yml
name: Validate Claude Hooks
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: python3 test_all_hooks.py
```

### DO: Version Control Hook Configurations
```bash
# Track hook changes
git add .claude/settings.json
git commit -m "Add production file protection hooks"
```

### DO: Share Best Practices with Team
- Create team hook templates
- Document common patterns
- Maintain shared MCP server list