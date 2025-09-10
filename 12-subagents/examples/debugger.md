# Debugger Subagent Example

This example demonstrates creating a specialized debugging subagent for error analysis, test failures, and unexpected behavior investigation.

## Subagent Configuration

**File**: `.claude/agents/debugger.md`

```markdown
---
name: debugger
description: Debugging specialist for errors, test failures, and unexpected behavior. Use proactively when encountering any issues.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert debugger specializing in root cause analysis.

When invoked:
1. Capture error message and stack trace
2. Identify reproduction steps
3. Isolate the failure location
4. Implement minimal fix
5. Verify solution works

Debugging process:
- Analyze error messages and logs
- Check recent code changes
- Form and test hypotheses
- Add strategic debug logging
- Inspect variable states

For each issue, provide:
- Root cause explanation
- Evidence supporting the diagnosis
- Specific code fix
- Testing approach
- Prevention recommendations

Focus on fixing the underlying issue, not just symptoms.
```

## Usage Scenarios

### Error Investigation

**User Input**:
```
> My API is returning 500 errors intermittently. The logs show "Object reference not set to an instance of an object"
```

**Subagent Process**:
1. Examines recent error logs
2. Identifies the specific code location
3. Analyzes variable states at failure point
4. Traces the null reference source
5. Provides targeted fix

### Test Failure Analysis

**User Input**:
```
> The integration tests are failing after my latest changes. Use the debugger subagent to investigate.
```

**Debugging Workflow**:
```
1. Run failed tests in isolation
2. Compare test output before/after changes
3. Identify breaking change location
4. Analyze test expectations vs actual behavior
5. Implement fix and verify test passes
```

### Performance Issue Investigation

**User Input**:
```
> The application is suddenly much slower. Can the debugger help identify what's causing the performance degradation?
```

## Sample Debugging Session

### Problem: Null Reference Exception

```
## Debugging Analysis

### Error Details
- **Exception**: NullReferenceException at UserService.GetUserProfile()
- **Frequency**: Intermittent, affecting ~5% of requests
- **Recent Changes**: Updated user authentication flow

### Investigation Steps

1. **Error Location Analysis**
   ```csharp
   // File: UserService.cs, Line 45
   var profile = user.Profile.DisplayName; // Null reference here
   ```

2. **Variable State Inspection**
   - `user` object is not null
   - `user.Profile` is null in failing cases
   - Profile should be loaded by UserRepository.GetUser()

3. **Root Cause Discovery**
   ```csharp
   // Issue in UserRepository.cs
   // Missing Include() for Profile navigation property
   var user = context.Users.FirstOrDefault(u => u.Id == userId);
   // Should be:
   var user = context.Users.Include(u => u.Profile).FirstOrDefault(u => u.Id == userId);
   ```

### Solution Implementation

```csharp
// Fix: Update UserRepository.GetUser method
public User GetUser(int userId)
{
    return context.Users
        .Include(u => u.Profile)  // Added missing Include
        .FirstOrDefault(u => u.Id == userId);
}
```

### Verification
- Unit test updated to verify Profile is loaded
- Integration test confirms fix resolves the issue
- No performance impact from additional Include

### Prevention Recommendations
- Add null checks for navigation properties
- Implement integration tests for all user flows
- Consider using required navigation properties in EF models
```

## Advanced Debugging Patterns

### Multi-Layer Debugging

```markdown
---
name: distributed-debugger
description: Debugging specialist for microservices and distributed systems. Use for issues spanning multiple services.
tools: Read, Edit, Bash, Grep, Glob
---

You are an expert at debugging distributed systems and microservice architectures.

Focus areas:
- Correlation ID tracking across services
- Network communication failures
- Data consistency issues
- Performance bottlenecks in distributed calls
- Service dependency analysis

Debugging approach:
1. Map the request flow across services
2. Identify failure points in the chain
3. Analyze logs with correlation IDs
4. Check service health and dependencies
5. Implement circuit breakers or retries as needed
```

### Frontend Debugging Specialist

```markdown
---
name: frontend-debugger
description: Frontend debugging specialist for React, TypeScript, and browser issues. Use for UI bugs, performance issues, and state management problems.
tools: Read, Edit, Bash, Grep, Glob
---

You are a frontend debugging expert specializing in modern web applications.

Common debugging scenarios:
- React component lifecycle issues
- State management bugs
- TypeScript compilation errors
- Browser compatibility problems
- Performance optimization

Debugging tools and techniques:
- Browser developer tools analysis
- React DevTools inspection
- Performance profiling
- Network request analysis
- Console error investigation
```

## Integration with Development Workflow

### Continuous Integration

```
> The CI pipeline is failing. Use the debugger subagent to analyze the build errors.
```

### Production Issue Response

```
> We have a production incident. The debugger subagent should investigate the error logs immediately.
```

### Development Troubleshooting

```
> This feature isn't working as expected. Have the debugger analyze what's going wrong.
```

## Best Practices for Debugging Subagents

### 1. Systematic Approach
- Always follow a consistent debugging methodology
- Document investigation steps for future reference
- Focus on root causes, not just symptoms

### 2. Evidence-Based Analysis
- Collect concrete evidence before proposing solutions
- Use logs, stack traces, and reproducible test cases
- Verify fixes with appropriate testing

### 3. Tool Access Management
- Grant debugging tools: Read, Edit, Bash, Grep, Glob
- Consider limiting Edit access for production debugging
- Provide access to logging and monitoring tools

### 4. Communication Style
- Provide clear, step-by-step analysis
- Include code examples and specific line references
- Offer prevention strategies for future occurrences

### 5. Specialization Benefits
- Create domain-specific debuggers (frontend, backend, database)
- Maintain separate contexts for different debugging sessions
- Enable focused expertise without context pollution

## Common Debugging Patterns

### Exception Analysis
1. Capture full stack trace
2. Identify the immediate cause
3. Trace back to root cause
4. Implement targeted fix
5. Add preventive measures

### Performance Investigation
1. Establish baseline metrics
2. Identify performance bottlenecks
3. Profile critical code paths
4. Implement optimizations
5. Validate improvements

### Integration Issue Resolution
1. Map data flow between components
2. Identify interface mismatches
3. Verify API contracts
4. Test integration points
5. Implement robust error handling

The debugger subagent provides focused expertise for problem resolution while maintaining clean separation from your main development workflow.