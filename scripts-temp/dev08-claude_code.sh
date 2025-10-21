#!/usr/bin/env bash
# install_claude.sh — automate installing, configuring, and verifying Claude Code CLI via npm

set -euo pipefail
IFS=$'\n\t'

# 1. Check for Node.js
if ! command -v node >/dev/null 2>&1; then
  echo "Error: Node.js is not installed. Please install Node.js 18+ and try again."
  exit 1
fi

# 2. Check for npm
if ! command -v npm >/dev/null 2>&1; then
  echo "Error: npm is not installed. Please install npm and try again."
  exit 1
fi

echo "Node.js version: $(node --version)"
echo "npm version:     $(npm --version)"

# 3. Install Claude Code globally via npm
echo "Installing @anthropic-ai/claude-code globally..."
npm install -g @anthropic-ai/claude-code

# 4. Prompt user for their Anthropic API key
read -r -p "Enter your ANTHROPIC_API_KEY: " CLAUDE_KEY
if [ -z "${CLAUDE_KEY// }" ]; then
  echo "Error: No API key entered."
  exit 1
fi

# 5. Determine which shell profile to update
#    Try ~/.bash_profile first, then ~/.profile
PROFILE="$HOME/.bash_profile"
if [ ! -f "$PROFILE" ]; then
  PROFILE="$HOME/.profile"
fi

# 6. Save API key into the profile
#    Remove any existing ANTHROPIC_API_KEY lines, then append new one
grep -v '^export ANTHROPIC_API_KEY=' "$PROFILE" 2>/dev/null > "${PROFILE}.tmp" || true
printf '\nexport ANTHROPIC_API_KEY="%s"\n' "$CLAUDE_KEY" >> "${PROFILE}.tmp"
mv "${PROFILE}.tmp" "$PROFILE"
echo "ANTHROPIC_API_KEY saved to $PROFILE"
echo "Reload it now with: source $PROFILE"

# 7. Disable auto-updates for Claude Code CLI
claude config set autoUpdates false --global

# 8. Verify installation and configuration
echo "Running 'claude doctor' to verify setup..."
claude doctor

# 9. Print usage instructions
cat << 'EOF'

Installation and configuration complete.

To start an interactive session:
  claude

To run a one-off command:
  claude --script "Explain the repo structure"

For full help:
  claude --help

EOF

exit 0
