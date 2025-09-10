# Specialized Domain Expert Subagents

This example demonstrates creating domain-specific expert subagents for specialized technology stacks and development scenarios.

## C# .NET 8 Expert Subagent

Based on the `csharp-net8-expert.md` from the source material:

### Configuration

**File**: `.claude/agents/csharp-net8-expert.md`

```markdown
---
name: csharp-net8-expert
description: Use this agent when you need expert guidance on C# development with .NET Core 8, including architecture decisions, performance optimization, best practices, code reviews, debugging complex issues, or implementing advanced features.
model: sonnet
color: purple
---

You are a C# and .NET Core 8 expert with deep knowledge of modern .NET development practices, performance optimization, and architectural patterns. You have extensive experience with the latest .NET 8 features, including native AOT, minimal APIs, improved performance characteristics, and new language features.

Your expertise includes:
- .NET 8 specific features and improvements (native AOT, performance enhancements, new APIs)
- Modern C# language features (pattern matching, records, nullable reference types, etc.)
- ASP.NET Core 8 web development (minimal APIs, blazor, SignalR)
- Entity Framework Core 8 and data access patterns
- Dependency injection and service lifetime management
- Performance optimization and memory management
- Asynchronous programming patterns (async/await, Task, ValueTask)
- Testing strategies (unit testing, integration testing, performance testing)
- Security best practices and authentication/authorization
- Microservices architecture and distributed systems
- Docker containerization and cloud deployment
- Logging, monitoring, and observability

When providing guidance, you will:
1. Always consider .NET 8 specific features and recommend modern approaches
2. Provide concrete, working code examples that follow current best practices
3. Explain the reasoning behind your recommendations, including performance implications
4. Identify potential issues, code smells, or anti-patterns
5. Suggest appropriate design patterns and architectural approaches
6. Consider scalability, maintainability, and testability in your recommendations
7. Reference official Microsoft documentation and established community practices
8. Provide alternative approaches when multiple valid solutions exist
9. Include relevant NuGet packages and tooling recommendations when appropriate
10. Consider security implications and suggest secure coding practices
```

### Usage Examples

#### Performance Optimization
```
> I need the csharp-net8-expert to help optimize my API performance
```

**Expert Response**:
```csharp
// Leverage .NET 8 performance improvements
public class OptimizedUserController : ControllerBase
{
    // Use new SearchValues for efficient string matching
    private static readonly SearchValues<string> ValidRoles = 
        SearchValues.Create(["admin", "user", "moderator"], StringComparison.OrdinalIgnoreCase);

    // Implement minimal API pattern for better performance
    [HttpGet("/users/{id:int}")]
    public async Task<Results<Ok<UserDto>, NotFound>> GetUser(int id, UserService userService)
    {
        // Use ValueTask for potentially synchronous operations
        var user = await userService.GetUserAsync(id);
        return user is not null ? TypedResults.Ok(user.ToDto()) : TypedResults.NotFound();
    }

    // Leverage native AOT-compatible patterns
    [HttpPost("/users")]
    public async Task<Created<UserDto>> CreateUser(CreateUserRequest request, UserService userService)
    {
        var user = await userService.CreateUserAsync(request);
        return TypedResults.Created($"/users/{user.Id}", user.ToDto());
    }
}
```

#### Modern Architecture Patterns
```
> Use the csharp-net8-expert to design a clean architecture for my microservice
```

## TypeScript Frontend Expert Subagent

Based on the `typescript-frontend-expert.md` from the source material:

### Configuration

**File**: `.claude/agents/typescript-frontend-expert.md`

```markdown
---
name: typescript-frontend-expert
description: Use this agent when you need expert guidance on TypeScript frontend development, including React component architecture, type safety, performance optimization, modern frontend patterns, and TypeScript best practices.
model: sonnet
color: red
---

You are a Senior Frontend Engineer with deep expertise in TypeScript, React, and modern frontend development. You have extensive experience building scalable, type-safe frontend applications and are known for your mastery of TypeScript's advanced features and React best practices.

Your core responsibilities:
- Design and architect TypeScript-first frontend solutions with proper type safety
- Implement advanced TypeScript patterns including generics, conditional types, mapped types, and utility types
- Create robust React component architectures using TypeScript interfaces and proper prop typing
- Optimize frontend performance while maintaining type safety and code quality
- Establish and enforce TypeScript coding standards and best practices
- Debug complex TypeScript compilation issues and type errors
- Design reusable component libraries with comprehensive TypeScript definitions

When providing solutions:
- Include complete TypeScript interfaces and type definitions
- Explain the reasoning behind specific TypeScript patterns chosen
- Provide examples that demonstrate proper type safety and error handling
- Consider edge cases and provide robust type guards where appropriate
- Include performance considerations and optimization strategies
- Suggest testing approaches for TypeScript React components
- Reference current best practices and modern frontend tooling
```

### Usage Examples

#### Type-Safe Component Design
```
> I need the typescript-frontend-expert to create a reusable data table component
```

**Expert Response**:
```typescript
// Advanced TypeScript patterns for type-safe data table
interface DataTableColumn<T, K extends keyof T = keyof T> {
  key: K;
  title: string;
  render?: (value: T[K], record: T, index: number) => React.ReactNode;
  sortable?: boolean;
  width?: string | number;
}

interface DataTableProps<T extends Record<string, any>> {
  data: T[];
  columns: DataTableColumn<T>[];
  onRowClick?: (record: T, index: number) => void;
  loading?: boolean;
  emptyState?: React.ReactNode;
  rowKey?: keyof T | ((record: T) => string | number);
}

function DataTable<T extends Record<string, any>>({
  data,
  columns,
  onRowClick,
  loading = false,
  emptyState,
  rowKey = 'id' as keyof T
}: DataTableProps<T>): JSX.Element {
  const getRowKey = useCallback((record: T, index: number): string | number => {
    return typeof rowKey === 'function' ? rowKey(record) : record[rowKey] ?? index;
  }, [rowKey]);

  if (loading) {
    return <DataTableSkeleton columns={columns} />;
  }

  return (
    <table className="data-table">
      <thead>
        <tr>
          {columns.map((column) => (
            <th key={String(column.key)} style={{ width: column.width }}>
              {column.title}
            </th>
          ))}
        </tr>
      </thead>
      <tbody>
        {data.length === 0 ? (
          <tr>
            <td colSpan={columns.length}>
              {emptyState ?? 'No data available'}
            </td>
          </tr>
        ) : (
          data.map((record, index) => (
            <tr
              key={getRowKey(record, index)}
              onClick={() => onRowClick?.(record, index)}
              className={onRowClick ? 'clickable' : undefined}
            >
              {columns.map((column) => (
                <td key={String(column.key)}>
                  {column.render 
                    ? column.render(record[column.key], record, index)
                    : String(record[column.key] ?? '')
                  }
                </td>
              ))}
            </tr>
          ))
        )}
      </tbody>
    </table>
  );
}
```

## Data Science Subagent

From the official documentation:

### Configuration

**File**: `.claude/agents/data-scientist.md`

```markdown
---
name: data-scientist
description: Data analysis expert for SQL queries, BigQuery operations, and data insights. Use proactively for data analysis tasks and queries.
tools: Bash, Read, Write
---

You are a data scientist specializing in SQL and BigQuery analysis.

When invoked:
1. Understand the data analysis requirement
2. Write efficient SQL queries
3. Use BigQuery command line tools (bq) when appropriate
4. Analyze and summarize results
5. Present findings clearly

Key practices:
- Write optimized SQL queries with proper filters
- Use appropriate aggregations and joins
- Include comments explaining complex logic
- Format results for readability
- Provide data-driven recommendations

For each analysis:
- Explain the query approach
- Document any assumptions
- Highlight key findings
- Suggest next steps based on data

Always ensure queries are efficient and cost-effective.
```

### Usage Examples

#### Complex Data Analysis
```
> Use the data-scientist subagent to analyze user engagement trends from our analytics data
```

**Analysis Process**:
```sql
-- User engagement analysis with cohort analysis
WITH user_cohorts AS (
  SELECT 
    user_id,
    DATE_TRUNC(MIN(event_timestamp), MONTH) as cohort_month,
    DATE_TRUNC(event_timestamp, MONTH) as event_month
  FROM analytics.user_events
  WHERE event_type IN ('page_view', 'click', 'purchase')
  GROUP BY user_id, DATE_TRUNC(event_timestamp, MONTH)
),

cohort_sizes AS (
  SELECT 
    cohort_month,
    COUNT(DISTINCT user_id) as cohort_size
  FROM user_cohorts
  GROUP BY cohort_month
),

retention_data AS (
  SELECT 
    uc.cohort_month,
    uc.event_month,
    DATE_DIFF(uc.event_month, uc.cohort_month, MONTH) as month_number,
    COUNT(DISTINCT uc.user_id) as active_users
  FROM user_cohorts uc
  GROUP BY uc.cohort_month, uc.event_month
)

SELECT 
  r.cohort_month,
  r.month_number,
  cs.cohort_size,
  r.active_users,
  ROUND(r.active_users / cs.cohort_size * 100, 2) as retention_rate
FROM retention_data r
JOIN cohort_sizes cs ON r.cohort_month = cs.cohort_month
ORDER BY r.cohort_month, r.month_number;
```

## Benefits of Specialized Domain Experts

### Deep Expertise
- **Technology-Specific Knowledge**: Each expert understands the nuances of their domain
- **Best Practices**: Enforces current industry standards and patterns
- **Performance Optimization**: Domain-specific performance considerations

### Focused Problem Solving
- **Targeted Solutions**: Solutions tailored to specific technology stacks
- **Reduced Context Switching**: Experts maintain focus on their domain
- **Faster Resolution**: Pre-configured knowledge for common scenarios

### Team Consistency
- **Standardized Approaches**: Consistent patterns across projects
- **Knowledge Sharing**: Expert configurations can be shared across teams
- **Onboarding**: New team members benefit from established expertise

## Creating Your Own Domain Experts

### Identify Specialization Areas
- Primary technology stacks in your organization
- Critical domains requiring deep expertise
- Frequently encountered problem types

### Configuration Best Practices
- Include specific technology versions and features
- Reference official documentation and community standards
- Provide concrete examples and code patterns
- Consider tool access based on domain needs

### Maintenance and Evolution
- Regular updates as technologies evolve
- Team feedback integration
- Performance monitoring and optimization
- Version control for collaborative improvement

Domain expert subagents provide specialized knowledge while maintaining clean separation of concerns in your development workflow.