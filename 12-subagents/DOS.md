# Subagents - Best Practices (DOS)

This document outlines best practices for creating, managing, and using subagents effectively in Claude Code.

## When to Use Subagents

### ✅ Ideal Use Cases

#### Specialized Domain Tasks
- **Code Reviews**: Consistent quality standards across all code changes
- **Debugging**: Systematic approach to error investigation and resolution  
- **Performance Analysis**: Focused expertise on optimization and profiling
- **Security Audits**: Specialized knowledge of security vulnerabilities and mitigations

#### Technology-Specific Expertise
- **Language Experts**: C#/.NET, TypeScript/React, Python/Django specialists
- **Platform Specialists**: AWS/Azure cloud experts, database optimization specialists
- **Framework Experts**: Frontend framework specialists, API design experts

#### Workflow Automation
- **Testing Specialists**: Automated test creation and failure analysis
- **Documentation Generators**: Consistent documentation standards and formats
- **Deployment Assistants**: CI/CD pipeline management and troubleshooting

### ✅ Context Management Benefits

#### Preserve Main Conversation Focus
```
✅ DO: Use subagents for detailed technical analysis
Main context: "I need to optimize the user dashboard performance"
Subagent context: Detailed performance profiling, code analysis, optimization implementation
```

#### Prevent Context Pollution
```
✅ DO: Delegate complex debugging to specialized subagents
Main context stays focused on feature development
Debugging subagent handles error logs, stack traces, and fix implementation
```

## Creating Effective Subagents

### ✅ Design Focused Responsibilities

#### Single Purpose Principle
```markdown
✅ DO: Create specific subagents
- code-reviewer: Only handles code quality analysis
- debugger: Only handles error investigation
- performance-optimizer: Only handles performance issues

❌ DON'T: Create generic "helper" subagents that try to do everything
```

#### Clear Expertise Boundaries
```markdown
✅ DO: Define clear domains
---
name: react-component-expert
description: React component architecture, TypeScript integration, and performance optimization specialist
---

❌ DON'T: Vague or overlapping responsibilities
---
name: frontend-helper
description: Helps with frontend stuff
---
```

### ✅ Write Detailed System Prompts

#### Include Specific Instructions
```markdown
✅ DO: Provide comprehensive guidance
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
```

#### Provide Examples and Context
```markdown
✅ DO: Include concrete examples
For TypeScript interfaces, always include:
- Proper generic constraints
- Optional vs required properties  
- JSDoc comments for complex types
- Export declarations for reusability

Example:
```typescript
interface DataTableProps<T extends Record<string, any>> {
  /** Array of data objects to display */
  data: T[];
  /** Column configuration with type safety */
  columns: DataTableColumn<T>[];
}
```
```

### ✅ Configure Tool Access Strategically

#### Principle of Least Privilege
```markdown
✅ DO: Grant only necessary tools
Code reviewer: Read, Grep, Glob, Bash (for git diff)
Documentation writer: Read, Write (no system modifications)
Debugger: Read, Edit, Bash, Grep, Glob (needs broader access)
```

#### Security Considerations
```markdown
✅ DO: Limit powerful tools to trusted subagents
Production debugger: Read, Grep, Glob only (no Edit, no Bash)
Development code-fixer: Full tool access for local development
Security auditor: Read-only access to prevent accidental changes
```

## Managing Subagents Effectively

### ✅ File Organization

#### Project vs User Scope
```
✅ DO: Choose appropriate scope
Project subagents (.claude/agents/): Team-specific, domain-specific
User subagents (~/.claude/agents/): Personal helpers, general utilities

✅ DO: Use descriptive filenames
.claude/agents/react-typescript-reviewer.md
.claude/agents/api-performance-optimizer.md
.claude/agents/database-migration-helper.md
```

#### Version Control Integration
```bash
✅ DO: Include project subagents in version control
git add .claude/agents/
git commit -m "Add team code review standards subagent"

✅ DO: Document subagent purpose in README
## Development Tools
- `.claude/agents/code-reviewer.md`: Enforces team coding standards
- `.claude/agents/test-generator.md`: Creates comprehensive test suites
```

### ✅ Naming Conventions

#### Use Descriptive Names
```markdown
✅ DO: Clear, purpose-driven names
name: typescript-react-expert
name: sql-performance-optimizer  
name: security-vulnerability-scanner

❌ DON'T: Generic or ambiguous names
name: helper
name: agent1
name: utility
```

#### Follow Naming Standards
```markdown
✅ DO: Use consistent patterns
Technology-expert pattern: python-expert, rust-expert
Task-specialist pattern: code-reviewer, test-generator, debugger
Domain-optimizer pattern: database-optimizer, api-optimizer
```

## Usage Patterns

### ✅ Encourage Proactive Use

#### Description Field Optimization
```markdown
✅ DO: Use action-oriented descriptions
description: "Expert code review specialist. Proactively reviews code for quality, security, and maintainability. Use immediately after writing or modifying code."

✅ DO: Include trigger phrases
"Use PROACTIVELY when..."
"MUST BE USED for..."
"Automatically invoke for..."
```

#### Context-Driven Activation
```markdown
✅ DO: Design for automatic delegation
User: "I just finished the authentication module"
System: Automatically invokes code-reviewer subagent

User: "The API is returning 500 errors"
System: Automatically invokes debugger subagent
```

### ✅ Explicit Invocation Patterns

#### Clear Request Syntax
```
✅ DO: Use explicit subagent requests
> Use the code-reviewer subagent to check my recent changes
> Have the debugger subagent investigate this error
> Ask the performance-optimizer subagent to analyze the slow endpoint
```

#### Chaining for Complex Workflows
```
✅ DO: Chain subagents for multi-step processes
> First use the code-analyzer subagent to find issues, then use the code-fixer subagent to resolve them
> Have the test-generator create tests, then use the test-runner to verify they pass
```

## Team Collaboration

### ✅ Shared Standards

#### Establish Team Conventions
```markdown
✅ DO: Create consistent team subagents
All projects use same code-reviewer configuration
Shared debugging approaches across team members
Consistent documentation generation standards
```

#### Regular Reviews and Updates
```markdown
✅ DO: Evolve subagents based on team learnings
Weekly review of subagent effectiveness
Update review criteria based on common issues found
Incorporate new best practices as they emerge
```

### ✅ Knowledge Sharing

#### Document Subagent Purpose
```markdown
✅ DO: Include team documentation
# Team Subagents

## code-reviewer
**Purpose**: Enforces team coding standards and security practices
**When to use**: After any code changes, before creating PRs
**Key focus**: Security, performance, maintainability

## api-designer  
**Purpose**: Ensures consistent API design patterns
**When to use**: When creating or modifying API endpoints
**Key focus**: RESTful design, error handling, documentation
```

## Performance Optimization

### ✅ Context Efficiency

#### Strategic Context Usage
```markdown
✅ DO: Design for efficient context usage
Subagents start with clean context - provide essential information quickly
Include relevant project patterns and constraints in system prompt
Cache common patterns in subagent configuration rather than re-explaining
```

#### Minimize Latency
```markdown
✅ DO: Optimize subagent startup
Include essential context in system prompt
Provide clear, specific tool requirements
Design for focused, single-purpose tasks
```

### ✅ Monitor and Measure

#### Track Subagent Effectiveness
```markdown
✅ DO: Evaluate subagent performance
Monitor how often subagents are used
Assess quality of subagent outputs
Gather team feedback on subagent helpfulness
Measure time savings from specialized assistance
```

## Security and Access Control

### ✅ Tool Permission Management

#### Production vs Development
```markdown
✅ DO: Differentiate environments
Development subagents: Full tool access for rapid iteration
Staging subagents: Limited write access, full read access
Production subagents: Read-only access, no system modifications
```

#### Sensitive Data Handling
```markdown
✅ DO: Protect sensitive information
Security auditor: No logging of sensitive data patterns
Code reviewer: Alert on potential secret exposure
Database analyzer: Anonymize sample data in examples
```

By following these best practices, you'll create effective, secure, and maintainable subagents that enhance your development workflow while preserving team consistency and code quality.