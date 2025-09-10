# Code Reviewer Subagent Example

This example demonstrates creating a comprehensive code review subagent that proactively reviews code for quality, security, and maintainability.

## Subagent Configuration

**File**: `.claude/agents/code-reviewer.md`

```markdown
---
name: code-reviewer
description: Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code.
tools: Read, Grep, Glob, Bash
---

You are a senior code reviewer ensuring high standards of code quality and security.

When invoked:
1. Run git diff to see recent changes
2. Focus on modified files
3. Begin review immediately

Review checklist:
- Code is simple and readable
- Functions and variables are well-named
- No duplicated code
- Proper error handling
- No exposed secrets or API keys
- Input validation implemented
- Good test coverage
- Performance considerations addressed

Provide feedback organized by priority:
- Critical issues (must fix)
- Warnings (should fix)
- Suggestions (consider improving)

Include specific examples of how to fix issues.
```

## Usage Examples

### Automatic Invocation

The subagent will be automatically invoked when:

```
> I just finished implementing the user authentication module, can you review it?
```

**Result**: Claude Code automatically uses the code-reviewer subagent based on the context.

### Explicit Invocation

You can explicitly request the code reviewer:

```
> Use the code-reviewer subagent to check my recent changes
> Have the code-reviewer subagent look at the UserService class
```

### Workflow Integration

```
> I've made changes to the payment processing logic. Review for security issues.
```

**Subagent Process**:
1. Runs `git diff` to identify recent changes
2. Focuses on payment-related files
3. Performs comprehensive security review
4. Provides categorized feedback

## Sample Review Output

```
## Code Review Results

### Critical Issues (Must Fix)
- **SQL Injection Risk**: Line 45 in PaymentService.cs uses string concatenation for SQL query
  ```csharp
  // Current (vulnerable)
  var query = $"SELECT * FROM payments WHERE userId = {userId}";
  
  // Fix with parameterized query
  var query = "SELECT * FROM payments WHERE userId = @userId";
  ```

### Warnings (Should Fix)
- **Missing Error Handling**: ProcessPayment method doesn't handle network timeouts
- **Hardcoded Values**: API endpoint URL should be in configuration

### Suggestions (Consider Improving)
- **Performance**: Consider caching payment methods for frequent lookups
- **Naming**: Variable `pm` could be more descriptive as `paymentMethod`
```

## Benefits Demonstrated

### Context Preservation
- Main conversation stays focused on high-level development tasks
- Code review details are handled in separate context
- Review history doesn't clutter main conversation

### Specialized Expertise
- Consistent review criteria across all code reviews
- Automated focus on security and performance
- Standardized feedback format

### Tool Access Control
- Limited to essential tools: Read, Grep, Glob, Bash
- No access to potentially destructive operations
- Focused on analysis and reporting

## Customization Options

### Project-Specific Rules

```markdown
---
name: code-reviewer
description: Expert code review specialist for React TypeScript projects. Focus on type safety and component patterns.
tools: Read, Grep, Glob, Bash
---

You are a senior React TypeScript code reviewer specializing in frontend best practices.

Additional focus areas:
- TypeScript type safety and proper interfaces
- React component patterns and hooks usage
- Performance optimization (memoization, lazy loading)
- Accessibility compliance
- CSS-in-JS best practices

Review React-specific patterns:
- Proper use of useEffect dependencies
- Component prop drilling vs context usage
- State management patterns
- Testing strategies for components
```

### Language-Specific Variants

You can create specialized reviewers for different languages:
- `code-reviewer-python.md` - Python-specific patterns
- `code-reviewer-go.md` - Go conventions and idioms
- `code-reviewer-rust.md` - Memory safety and ownership patterns

## Integration with Development Workflow

### Pre-commit Reviews
```
> Before I commit these changes, have the code-reviewer check them
```

### Pull Request Preparation
```
> I'm about to create a PR for the new feature. Review the implementation first.
```

### Continuous Improvement
```
> The code-reviewer found issues last time. Check if I've addressed them properly.
```

## Best Practices

1. **Descriptive Names**: Use clear, purpose-driven naming for subagents
2. **Focused Scope**: Keep review criteria specific and actionable
3. **Tool Limitation**: Only grant necessary tools for security
4. **Team Consistency**: Share project-level subagents for consistent standards
5. **Regular Updates**: Refine review criteria based on team learnings