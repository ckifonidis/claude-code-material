---
description: Generate comprehensive code review for a file or directory
argument-hint: [file-path] [focus: security|performance|maintainability]
allowed-tools: Read, Grep, Bash(git log:*), Bash(git diff:*)
---

# Code Review Request

## Context
Current git status: !`git status --porcelain`
Recent commits affecting this area: !`git log --oneline -5 -- $1`

## Your Task
Perform a thorough code review of @$1 with focus on $2 aspects.

## Review Guidelines
- Analyze code structure, patterns, and conventions
- Identify potential bugs, security issues, or performance problems
- Check for adherence to best practices
- Suggest specific improvements with examples
- Consider maintainability and readability
- Highlight any breaking changes or compatibility issues

## Focus Areas
Focus particularly on: **$2**

Please provide:
1. **Summary** - Overall assessment and key findings
2. **Issues Found** - Specific problems with line references
3. **Recommendations** - Actionable improvement suggestions
4. **Positive Aspects** - Good practices worth highlighting