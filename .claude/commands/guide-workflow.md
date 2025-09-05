---
argument-hint: [section-number] [content]
description: Enhanced Claude Code guide workflow with intelligent content processing and placement
allowed-tools: Read, Edit, Write, MultiEdit, TodoWrite, Glob
---

# Enhanced Claude Code Guide - Section Workflow

## Context

Reading the current workflow prompt and progress files:

- Workflow instructions: @WORKFLOW-PROMPT.md
- Current progress: @PROGRESS.md
- Project instructions: @CLAUDE.md

## Your Task

You are helping with the Claude Code guide development with enhanced content processing capabilities.

### Mode 1: Status Overview (No Arguments)
**If no section number provided ($ARGUMENTS is empty):**
- Display the current section status from PROGRESS.md
- Show available sections 1-13 with their current status
- Ask the user to select a section number to work on

### Mode 2: Section Selection (Section Number Only)
**If only section number provided (e.g., "1", "5", "12"):**
1. Check PROGRESS.md for the specific section's current status and requirements
2. Read the section's README.md file to see current content
3. Display:
   - Section title and current status
   - Core requirements (always required)
   - Optional requirements for this specific section
   - What's already completed vs what needs work
4. **Prompt for content**: Ask user to provide content they want to add to this section
5. Explain that you'll analyze and improve their content before placing it correctly

### Mode 3: Content Processing (Section Number + Content)
**If section number AND content provided:**

#### Step 1: Content Analysis
Analyze the provided content to determine:
- **Content Type**: Concepts, procedures, examples, references, best practices
- **Content Quality**: Clarity, completeness, formatting needs
- **Key Concepts**: Essential information that must be preserved
- **Content Gap**: Missing information or unclear areas

#### Step 2: Content Classification
Determine which README subsection the content belongs to:
- **Introduction (## Introduction)**: Overview, purpose, context-setting information
- **Main Content (## [Section-specific title])**: Core concepts, detailed explanations, procedures, methodologies
- **Documentation References (## References to Official Documentation)**: Links, official docs, external resources
- **Examples Directory**: Code samples, workflows, use cases (create separate .md files)

#### Step 3: Content Enhancement
Improve the content by:
- **Structure**: Add proper markdown formatting, headings, bullet points, code blocks
- **Clarity**: Simplify complex sentences, improve readability, fix grammar
- **Conciseness**: Remove redundancy while preserving all key concepts
- **Consistency**: Match existing guide tone, style, and formatting conventions
- **Completeness**: Identify gaps and ask for clarification if needed

#### Step 4: Intelligent Placement
1. Read the current README.md content for the section
2. Determine exact placement within the identified subsection
3. Show the user:
   - Which subsection you'll update
   - The improved content
   - How it will be integrated with existing content
4. Ask for confirmation before making changes

#### Step 5: README Update
If user confirms:
1. Use Edit or MultiEdit to update the appropriate README.md file
2. Preserve existing content structure
3. Integrate new content seamlessly
4. Ensure proper markdown formatting

#### Step 6: Progress Tracking
1. Update TodoWrite with completed work
2. Check if section requirements are now met
3. Offer to update PROGRESS.md if section is complete
4. Suggest next steps or additional content needs

### Interactive Clarification Workflow

**When content needs improvement, ask targeted questions:**
- "This content seems to cover [concept]. Could you provide more details about [specific aspect]?"
- "The content mentions [topic] but doesn't explain [missing piece]. Can you elaborate?"
- "Should this be placed in [subsection A] or [subsection B]? The content could fit in either."
- "This content would benefit from an example. Do you have a specific use case in mind?"

**Quality Gates:**
- If content is unclear or incomplete, request clarification before proceeding
- If placement is ambiguous, ask user to confirm the intended subsection
- If content doesn't match section theme, suggest alternative placement

### Section Structure Requirements
- **Core Requirements**: Introduction subsection, Main subsection, Official documentation references
- **Optional Requirements**: Examples, DOS.md, DONTS.md (varies by section)
- **Quality Standards**: Clear, concise, well-formatted, technically accurate

### Content Processing Examples

**Example 1: Concept Content**
```
User Input: "AI assistance helps developers code faster by suggesting completions and finding bugs automatically"

Analysis: Core concept explanation
Classification: Main content subsection
Enhancement: Expand with benefits, methodology, use cases
Placement: "## Understanding AI-Assisted Development" subsection
```

**Example 2: Reference Content**
```
User Input: "See Claude Code docs at docs.anthropic.com"

Analysis: Documentation reference
Classification: References subsection  
Enhancement: Format as proper link with description
Placement: "## References to Official Documentation" subsection
```

### Remember
- **Always preserve key concepts** from user input
- **Improve formatting and clarity** without changing meaning
- **Ask for clarification** when content is ambiguous or incomplete
- **Confirm placement** before making README changes
- **Track progress** and update completion status
- **Work collaboratively** with the user throughout the process

This enhanced workflow transforms raw content input into polished, properly-placed guide sections while maintaining collaborative control over the development process.