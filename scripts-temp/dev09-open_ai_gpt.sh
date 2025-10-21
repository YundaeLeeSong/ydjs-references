#!/usr/bin/env bash
# install_openai_cli.sh — install OpenAI CLI, configure API key, verify access, and test best-available GPT model

if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi


set -euo pipefail
IFS=$'\n\t'

########################################
# 1. Prerequisite checks
########################################

on_pvm

echo "Using $(python --version) and $(pip --version)"

########################################
# 2. Install or upgrade OpenAI CLI
########################################

pip install --upgrade openai

########################################
# 3. Prompt for API key and save it
########################################

read -r -p "Enter your OpenAI API key (sk-...): " OPENAI_KEY
if [ -z "${OPENAI_KEY// }" ]; then
  echo "Error: No API key entered."
  exit 1
fi

# Choose shell profile to update
PROFILE="$HOME/.bash_profile"
[ ! -f "$PROFILE" ] && PROFILE="$HOME/.profile"

# Remove old key lines, then append new
grep -v '^export OPENAI_API_KEY=' "$PROFILE" 2>/dev/null > "${PROFILE}.tmp" || true
printf '\nexport OPENAI_API_KEY="%s"\n' "$OPENAI_KEY" >> "${PROFILE}.tmp"
mv "${PROFILE}.tmp" "$PROFILE"
echo "Saved OPENAI_API_KEY to $PROFILE"
echo "Run: source $PROFILE"

########################################
# 4. Verify installation
########################################

if ! command -v openai >/dev/null 2>&1; then
  echo "Error: openai CLI not found after install."
  exit 1
fi

echo "openai CLI version: $(openai -V)"

########################################
# 5. Detect accessible models
########################################

echo "Fetching list of available models..."
MODEL_LIST_JSON=$(OPENAI_API_KEY="$OPENAI_KEY" openai api models.list)
# Extract model ids into a simple list
MODEL_IDS=$(printf '%s' "$MODEL_LIST_JSON" | grep -oP '"id":\s*"\K[^"]+')

# Choose preferred model
if printf '%s\n' $MODEL_IDS | grep -xq 'gpt-4'; then
  SELECTED_MODEL="gpt-4"
elif printf '%s\n' $MODEL_IDS | grep -xq 'gpt-3.5-turbo'; then
  SELECTED_MODEL="gpt-3.5-turbo"
else
  echo "Warning: neither gpt-4 nor gpt-3.5-turbo found."
  # Fallback to the first model in the list
  SELECTED_MODEL=$(printf '%s\n' $MODEL_IDS | head -n1)
  echo "Falling back to: $SELECTED_MODEL"
fi

echo "Selected model for test: $SELECTED_MODEL"

########################################
# 6. Test a simple chat completion
########################################

TEST_PAYLOAD='{"messages":[{"role":"user","content":"Hello, who are you?"}]}'

echo "Testing chat completion with $SELECTED_MODEL..."
set +e
RESPONSE_RAW=$(OPENAI_API_KEY="$OPENAI_KEY" openai api chat.completions.create \
  -m "$SELECTED_MODEL" \
  -j "$TEST_PAYLOAD" 2>&1)
STATUS=$?
set -e

if [ $STATUS -ne 0 ]; then
  echo "Error during test call:"
  echo "$RESPONSE_RAW"
  exit 1
fi

# Extract and display the assistant's content
ASSISTANT_CONTENT=$(printf '%s' "$RESPONSE_RAW" | grep -oP '"content":\s*"\K([^"]|\\")*')
echo "Response from API:"
echo "$ASSISTANT_CONTENT"

########################################
# 7. Final instructions
########################################

cat << 'EOF'

Setup complete.

To run a chat:
  openai api chat.completions.create \
    -m MODEL_NAME \
    -g user "Your message here"

Or with JSON:
  openai api chat.completions.create \
    -m MODEL_NAME \
    -j '{"messages":[{"role":"user","content":"Your message"}]}'

Replace MODEL_NAME with one of:
  - gpt-4
  - gpt-3.5-turbo
  - any other model you have access to

For help:
  openai --help
  openai api chat.completions.create --help

EOF

exit 0

OPENAI_API_KEY="$OPENAI_API_KEY" openai api chat.completions.create \
  -m "gpt-3.5-turbo" \
  -g system "You are a helpful assistant." \
  -g user   "Hello, who are you?"
