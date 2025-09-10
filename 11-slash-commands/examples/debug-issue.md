---
description: Debug and analyze code issues with systematic investigation
argument-hint: [issue-description] [file-path-optional]
allowed-tools: Read, Grep, Bash(git log:*), Bash(git diff:*), Bash(npm test:*), Bash(git blame:*)
model: claude-3-5-sonnet-20241022
---

# Debug Issue Investigation

## Context
Issue description: $1
Target area: @$2
Current status: !`git status --porcelain`
Recent changes: !`git log --oneline -5 $2`

## Your Task
Systematically debug and analyze the following issue: **$1**

## Investigation Steps

### 1. Problem Analysis
- Understand the issue description and expected vs actual behavior
- Identify the scope and impact of the problem
- Determine if this is a regression or new issue

### 2. Code Examination
- Review relevant code sections in @$2
- Check for recent changes that might have introduced the issue: !`git log --oneline -10 -- $2`
- Examine error patterns and edge cases

### 3. Root Cause Analysis
- Trace the execution flow
- Identify potential causes (logic errors, race conditions, data issues, etc.)
- Check for similar patterns in the codebase

### 4. Testing Strategy
- Suggest test cases to reproduce the issue
- Recommend existing tests to run: !`find . -name "*test*" -type f | head -5`
- Propose new tests to prevent regression

## Debugging Guidelines
- Use systematic approach: reproduce → isolate → identify → fix
- Consider all possible causes before suggesting solutions
- Look for patterns in logs, error messages, and user reports
- Check dependencies and environment factors
- Verify assumptions with actual data

## Expected Output
Provide:
1. **Root Cause** - Clear explanation of what's causing the issue
2. **Fix Strategy** - Step-by-step solution approach
3. **Test Plan** - How to verify the fix works
4. **Prevention** - How to avoid similar issues in the future

If code location not specified with $2, help identify where to look based on the issue description.