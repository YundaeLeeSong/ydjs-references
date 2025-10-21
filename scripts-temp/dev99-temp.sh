#!/bin/bash
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
else
    echo -e "\033[1;31mError: ~/.bashrc not found. Exiting...\033[0m"
    exit 1
fi

echo "#1: $(TEST_PASS 'All tests passed successfully!')"
echo "#2: $(TEST_FAIL 'Error: Could not connect to the database!')"
echo "#3: $(USRPROMPT 'Prompt: Do the following actions')"
echo "#4: $(DEBUG_USR 'User-level debug: Input parameters are valid.')"
echo "#5: $(DEBUG_SYS 'System-level debug: Memory allocation successful.')"

echo "Hello, World! (Bash)"
echo "HOME directory: $HOME"
echo "Current directory: $(pwd)"
read -p "Press Enter to continue..."
exit