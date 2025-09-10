# Subagents

## Introduction
This section covers the use of specialized subagents in Claude Code, explaining when and how to leverage different agent types for specific development tasks.

## Specialized Agent Usage

Subagents are pre-configured AI personalities that Claude Code can delegate tasks to for more efficient problem-solving. Each subagent provides task-specific configurations with customized system prompts, tools, and a separate context window.

### What are Subagents?

Subagents are specialized AI assistants that operate independently from the main Claude Code conversation. Each subagent:

- **Has a specific purpose and expertise area** - Focused on particular types of tasks or domains
- **Uses its own context window** - Separate from the main conversation to prevent context pollution
- **Can be configured with specific tools** - Only the tools necessary for its designated purpose
- **Includes a custom system prompt** - Guides its behavior and approach to problem-solving

When Claude Code encounters a task that matches a subagent's expertise, it can delegate that task to the specialized subagent, which works independently and returns results.

### Key Benefits

#### Context Preservation
Each subagent operates in its own context, preventing pollution of the main conversation and keeping it focused on high-level objectives.

#### Specialized Expertise
Subagents can be fine-tuned with detailed instructions for specific domains, leading to higher success rates on designated tasks.

#### Reusability
Once created, subagents can be used across different projects and shared with your team for consistent workflows.

#### Flexible Permissions
Each subagent can have different tool access levels, allowing you to limit powerful tools to specific subagent types.

### Creating and Managing Subagents

#### Quick Start with /agents Command

To create your first subagent:

1. **Open the subagents interface**:
   ```
   /agents
   ```

2. **Select 'Create New Agent'**: Choose whether to create a project-level or user-level subagent

3. **Define the subagent**:
   - **Recommended**: Generate with Claude first, then customize to make it yours
   - Describe your subagent in detail and when it should be used
   - Select the tools you want to grant access to (or leave blank to inherit all tools)
   - The interface shows all available tools, making selection easy
   - If generating with Claude, you can edit the system prompt in your editor by pressing `e`

4. **Save and use**: Your subagent is now available! Claude will use it automatically when appropriate

#### File Structure and Configuration

Subagents are stored as Markdown files with YAML frontmatter in two possible locations:

| Type | Location | Scope | Priority |
|------|----------|-------|----------|
| **Project subagents** | `.claude/agents/` | Available in current project | Highest |
| **User subagents** | `~/.claude/agents/` | Available across all projects | Lower |

When subagent names conflict, project-level subagents take precedence over user-level subagents.

#### File Format

Each subagent is defined in a Markdown file with this structure:

```markdown
---
name: your-sub-agent-name
description: Description of when this subagent should be invoked
tools: tool1, tool2, tool3  # Optional - inherits all tools if omitted
---

Your subagent's system prompt goes here. This can be multiple paragraphs
and should clearly define the subagent's role, capabilities, and approach
to solving problems.

Include specific instructions, best practices, and any constraints
the subagent should follow.
```

**Configuration fields:**

| Field | Required | Description |
|-------|----------|-------------|
| `name` | Yes | Unique identifier using lowercase letters and hyphens |
| `description` | Yes | Natural language description of the subagent's purpose |
| `tools` | No | Comma-separated list of specific tools. If omitted, inherits all tools from the main thread |

### Using Subagents Effectively

#### Automatic Delegation

Claude Code proactively delegates tasks based on:
- The task description in your request
- The `description` field in subagent configurations
- Current context and available tools

**Tip**: To encourage more proactive subagent use, include phrases like "use PROACTIVELY" or "MUST BE USED" in your `description` field.

#### Explicit Invocation

Request a specific subagent by mentioning it in your command:

```
> Use the test-runner subagent to fix failing tests
> Have the code-reviewer subagent look at my recent changes
> Ask the debugger subagent to investigate this error
```

### Advanced Usage Patterns

#### Chaining Subagents

For complex workflows, you can chain multiple subagents:

```
> First use the code-analyzer subagent to find performance issues, then use the optimizer subagent to fix them
```

#### Dynamic Subagent Selection

Claude Code intelligently selects subagents based on context. Make your `description` fields specific and action-oriented for best results.

#### Tool Access Management

You have two options for configuring tools:
- **Omit the `tools` field** to inherit all tools from the main thread (default), including MCP tools
- **Specify individual tools** as a comma-separated list for more granular control

**MCP Integration**: Subagents can access MCP tools from configured MCP servers. When the `tools` field is omitted, subagents inherit all MCP tools available to the main thread.

### Performance Considerations

#### Context Efficiency
Subagents help preserve main context, enabling longer overall sessions by preventing context pollution.

#### Latency Considerations
Subagents start with a clean slate each time they are invoked and may add latency as they gather context required to do their job effectively.

#### Memory Management
Each subagent operates independently, which means better memory isolation but requires context re-establishment for each invocation.

### Integration with Development Workflows

#### Version Control Integration
Check project subagents into version control so your team can benefit from and improve them collaboratively.

#### Team Collaboration
Project-level subagents enable consistent workflows across team members and can be shared and refined collectively.

#### CI/CD Integration
Subagents can be designed to work with automated workflows, providing specialized assistance for testing, deployment, and code review processes.

## References to Official Documentation
- [Subagents Overview](https://docs.anthropic.com/en/docs/claude-code/subagents) - Complete guide to creating and using specialized AI subagents