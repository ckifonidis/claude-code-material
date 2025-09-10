# Slash Commands - Best Practices (DOS)

This document outlines best practices for creating and using custom slash commands in Claude Code.

## Command Design Best Practices

### DO: Create Clear, Purposeful Commands

✅ **Use descriptive names that indicate the command's purpose**
```bash
# Good
/review-pr
/generate-docs
/security-audit

# Avoid
/cmd1
/helper
/do-stuff
```

✅ **Write clear descriptions and argument hints**
```markdown
---
description: Review pull request with security focus
argument-hint: [pr-number] [reviewer]
---
```

### DO: Structure Commands for Reusability

✅ **Use argument placeholders effectively**
```markdown
# Flexible - works with any issue number
Fix issue #$ARGUMENTS following our coding standards

# Structured - specific parameter roles
Review PR #$1 with priority $2 and assign to $3
```

✅ **Design commands that work across different contexts**
```markdown
# Works for any file type
Generate comprehensive documentation for @$1
```

### DO: Organize Commands Logically

✅ **Use project vs personal commands appropriately**
- **Project commands** (`.claude/commands/`) for team-shared workflows
- **Personal commands** (`~/.claude/commands/`) for individual preferences

✅ **Use directory namespacing for organization**
```
.claude/commands/
├── frontend/
│   ├── component.md
│   └── test.md
├── backend/
│   ├── api.md
│   └── deploy.md
└── docs/
    └── generate.md
```

### DO: Implement Proper Context Gathering

✅ **Include relevant context using bash commands**
```markdown
---
allowed-tools: Bash(git status:*), Bash(git diff:*)
---

Current state: !`git status --porcelain`
Recent changes: !`git diff HEAD~1`
```

✅ **Reference files when needed**
```markdown
# Review the current implementation
Analyze @src/main.js and suggest improvements
```

### DO: Follow Security Best Practices

✅ **Only request necessary tools**
```markdown
---
# Only allow specific git commands
allowed-tools: Bash(git status:*), Bash(git diff:*), Bash(git add:*)
---
```

✅ **Be explicit about tool permissions**
```markdown
---
# Specific file operations only
allowed-tools: Read, Write(/specific/path/*), Bash(npm test:*)
---
```

✅ **Avoid exposing sensitive information**
```markdown
# Good - doesn't expose credentials
Check deployment status without revealing secrets

# Avoid - might expose sensitive data
Display all environment variables: !`env`
```

## Usage Best Practices

### DO: Test Commands Thoroughly

✅ **Test with different argument patterns**
```bash
/review-pr 123
/review-pr 123 alice
/review-pr 123 alice urgent
```

✅ **Verify file references work correctly**
```bash
/docs src/utils/helpers.js
/docs "src/file with spaces.js"
/docs src/
```

### DO: Create Commands for Repetitive Tasks

✅ **Automate frequent workflows**
- Code review requests
- Bug investigation procedures
- Documentation generation
- Deployment checklists

✅ **Standardize team processes**
- Commit message formatting
- PR creation templates
- Security audit checklists

### DO: Use Frontmatter Effectively

✅ **Specify appropriate models for different tasks**
```markdown
---
model: claude-3-5-haiku-20241022  # For simple, fast tasks
---

---
model: claude-3-5-sonnet-20241022  # For complex analysis
---
```

✅ **Provide helpful argument hints**
```markdown
---
argument-hint: add [task] | remove [id] | list
---

---
argument-hint: [file-path] [priority: low|medium|high]
---
```

## Command Maintenance Best Practices

### DO: Keep Commands Updated

✅ **Review and update commands regularly**
- Remove obsolete commands
- Update tool permissions as needed
- Refine prompts based on usage patterns

✅ **Document command purposes**
```markdown
---
description: Generate API documentation from OpenAPI specs
# Last updated: 2024-01-15
# Purpose: Replaces manual documentation workflow
---
```

### DO: Share Effective Commands

✅ **Commit useful project commands to version control**
- Team members can benefit from shared workflows
- Standardizes development processes

✅ **Document command usage in project README**
```markdown
## Available Slash Commands

- `/review-pr [number]` - Generate PR review request
- `/deploy [environment]` - Deploy to specified environment
- `/docs [file]` - Generate documentation for file
```

## Performance Best Practices

### DO: Optimize Command Execution

✅ **Minimize bash command usage**
```markdown
# Good - only essential context
Current branch: !`git branch --show-current`

# Avoid - unnecessary information
!`find . -name "*.js" | wc -l`
!`du -sh *`
!`ps aux`
```

✅ **Use specific file references**
```markdown
# Good - targeted analysis
Review @src/auth/login.js for security issues

# Less efficient - too broad
Review @src/ for security issues
```

### DO: Design for Scalability

✅ **Create commands that work with growing codebases**
```markdown
# Scales well - focuses on specific areas
Analyze recent changes in @$1 for potential issues

# May not scale - analyzes everything
Review entire codebase for issues
```

## Quality Assurance

### DO: Follow Consistent Patterns

✅ **Use consistent formatting across commands**
```markdown
## Context
[Context gathering section]

## Your Task
[Clear task description]

## Guidelines
[Specific requirements or constraints]
```

✅ **Maintain consistent naming conventions**
- Use kebab-case for command names (`review-pr`, not `reviewPr`)
- Use clear, action-oriented verbs (`generate`, `review`, `analyze`)

Following these best practices will help you create effective, maintainable, and secure slash commands that enhance your development workflow.