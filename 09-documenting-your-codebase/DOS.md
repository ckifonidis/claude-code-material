# Documentation Best Practices (DOS)

## DO: Start with Architecture Overview

✅ **Begin documentation efforts with high-level architecture**
```bash
> document the main architecture and components of this project
> explain the key data models and their relationships
> describe the main workflow and data flow
```

## DO: Maintain Consistency

✅ **Follow existing documentation patterns in your project**
```bash
> find the documentation style used in this project
> update all function documentation to follow our JSDoc template
> ensure all API endpoints use the same documentation format
```

## DO: Include Practical Examples

✅ **Always provide usage examples in documentation**
```bash
> add usage examples to all public API functions
> create code snippets showing common use cases
> include both simple and complex examples
```

## DO: Document Edge Cases

✅ **Document error handling and edge cases**
```bash
> document all error scenarios for this API
> add information about rate limits and constraints
> include troubleshooting guides for common issues
```

## DO: Keep Documentation Current

✅ **Update documentation alongside code changes**
```bash
> update the documentation to reflect the changes in PR #123
> find documentation that doesn't match current implementation
> sync API docs with the latest endpoint changes
```

## DO: Use Automated Documentation Checks

✅ **Integrate documentation validation in CI/CD**
```json
{
  "scripts": {
    "docs:check": "claude -p 'verify all public functions have documentation'",
    "docs:lint": "claude -p 'check documentation for grammar and clarity issues'",
    "docs:coverage": "claude -p 'report documentation coverage percentage'"
  }
}
```

## DO: Document Dependencies

✅ **Clearly document all dependencies and requirements**
```bash
> document all external dependencies and their purposes
> add installation requirements to the README
> document environment variables and configuration options
```

## DO: Create Migration Guides

✅ **Provide migration guides for breaking changes**
```bash
> create a migration guide from v1 to v2
> document all breaking changes in the changelog
> provide code examples for migrating deprecated features
```

## DO: Use Semantic Documentation

✅ **Make documentation searchable and semantic**
```bash
> add keywords and tags to documentation for better searchability
> use consistent terminology throughout the documentation
> create a glossary of project-specific terms
```

## DO: Document Performance Considerations

✅ **Include performance implications in documentation**
```bash
> document the performance characteristics of this algorithm
> add notes about memory usage and optimization opportunities
> include benchmarks and performance testing results
```

## DO: Leverage Claude Code's Multi-Format Support

✅ **Use appropriate documentation formats for different contexts**
- JSDoc for JavaScript/TypeScript
- Docstrings for Python
- XML comments for C#
- Markdown for README files
- OpenAPI for REST APIs

## DO: Create Interactive Documentation

✅ **Generate interactive documentation when possible**
```bash
> create Swagger UI configuration for the API
> generate interactive Jupyter notebooks for data processing
> create Storybook stories for UI components
```

## DO: Document Security Considerations

✅ **Include security notes in sensitive areas**
```bash
> add security considerations to authentication documentation
> document data privacy requirements
> include notes about input validation and sanitization
```

## DO: Batch Documentation Tasks

✅ **Process multiple documentation tasks efficiently**
```bash
# Instead of individual requests:
> document function A
> document function B
> document function C

# Use batch processing:
> document all public functions in the auth module
```

## DO: Version Your Documentation

✅ **Maintain documentation versions aligned with code versions**
```bash
> tag documentation with version 2.0.0
> maintain separate docs for v1 and v2 APIs
> clearly mark deprecated features in documentation
```