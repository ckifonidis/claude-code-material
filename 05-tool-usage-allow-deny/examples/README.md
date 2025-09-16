# Settings Examples

This directory contains example `settings.json` files that you can copy to your `.claude/` directory.

## Git-Only Example

**File**: `git-settings.json`

A simple example that allows basic git operations while asking for confirmation on push/pull:

```bash
# Copy to your project
cp git-settings.json /path/to/your/project/.claude/settings.json

# Or copy to global settings
cp git-settings.json ~/.claude/settings.json
```

**What it allows automatically:**
- `git status`
- `git diff`
- `git log`
- `git add` (any files)
- `git commit` (any message)

**What requires confirmation:**
- `git push` (any branch)
- `git pull` (any branch)

**What is blocked:**
- Reading `.env` files
- Reading `.env.*` files

This is a minimal, safe starting point for git workflows with Claude Code.