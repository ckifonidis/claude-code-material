---
argument-hint: [section-number]
description: Start working on a Claude Code guide section using the structured workflow
allowed-tools: Read, Edit, Write, MultiEdit, TodoWrite
---

# Claude Code Guide - Section Workflow

## Context

Reading the current workflow prompt and progress files:

- Workflow instructions: @WORKFLOW-PROMPT.md
- Current progress: @PROGRESS.md
- Project instructions: @prompt.md

## Your Task

You are helping with the Claude Code guide development. 

**If no section number provided ($ARGUMENTS is empty):**
- Display the current section status from PROGRESS.md
- Show available sections 1-13 with their current status
- Ask the user to select a section number to work on

**If section number provided ($ARGUMENTS):**
1. Check PROGRESS.md for the specific section's current status and requirements
2. Read the section's README.md file to see current content
3. Display:
   - Section title and current status
   - Core requirements (always required)
   - Optional requirements for this specific section
   - What's already completed vs what needs work
4. Ask what content they want to work on for this section
5. As work progresses, update progress tracking using TodoWrite
6. When section requirements are met, offer to mark the section as complete in PROGRESS.md

**Section Structure Requirements:**
- Every section needs: Introduction subsection, Main subsection, Official documentation references
- Some sections need examples, DOS.md, DONTS.md based on section type
- Follow the evaluation criteria in prompt.md

**Remember:**
- Use the TodoWrite tool to track progress on tasks
- Not all sections need examples - evaluate individually  
- Always check current content before suggesting changes
- Update PROGRESS.md when sections are completed
- Work collaboratively with the user on content placement