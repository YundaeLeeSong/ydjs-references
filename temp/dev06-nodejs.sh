#!/bin/bash
BASHRC_PATH="$HOME/.bashrc" # Check if .bashrc exists, create if missing
if [[ -f "$BASHRC_PATH" ]]; then
    echo ".bashrc exists at: $BASHRC_PATH."
else
    echo ".bashrc not found. Creating a new one at: $BASHRC_PATH."
    cat <<EOL > "$BASHRC_PATH"
# ~/.bashrc
# Add your custom configurations here.

EOL
fi

TITLE="Node JS"
CONFIG="General configuration for '${TITLE}'" # configuration title
MARKER="?NODEJS;" # Check if the configuration script exists in ~/.bashrc
SCRIPT=$(cat <<'EOF'

################################################################################
#                                   ?NODEJS;
################################################################################
#################################< VERSION >####################################
NODE_VERSIONS=("v18.12.0" "v20.9.0")
NODE_VERSIONS=("v20.9.0")
NODE_VERSIONS=("v18.12.0")
##################################< USAGE >#####################################
# ### language system setup ... (1)
# enable_nodejs
###############################################################################
NODE_URL="https://nodejs.org/dist/{VERSION}/node-{VERSION}-win-x64.zip"
NODE_DIR="${PROJ_EXT}/node-{VERSION}-win-x64"
function enable_nodejs {
    # NODE checkup (positive)
    if exists "$PROJ_EXT" "node"; then
        echo "Notice: Directory $(USRPROMPT ''${NODE_DIR}' ')already exists. NODE has been setup..."
        # NODE setup
        SETUP_NODE
        return
    fi
    # NODE install
    for ver in "${NODE_VERSIONS[@]}"; do
        url="${NODE_URL//\{VERSION\}/$ver}"
        INSTRACT "$url" "node.zip" "${PROJ_EXT}"
    done
    # NODE checkup (negative)
    if [[ ! -d "$PROJ_EXT" ]]; then
        echo "Error: $(TEST_FAIL 'There is no '${PROJ_EXT}' found.')"
        return
    fi
    # NODE setup
    SETUP_NODE
}
function SETUP_NODE {
    for ver in "${NODE_VERSIONS[@]}"; do
        echo "${NODE_DIR//\{VERSION\}/$ver}:${PATH}"
        export PATH="${NODE_DIR//\{VERSION\}/$ver}:${PATH}"
    done
    node -v # Node.js
    npm -v # Node Package Manager (npm)
    npx -v # Node Package eXecutor (npx) to execute Node.js binaries or scripts directly from the command line without globally installing them
}

EOF
)
if ! grep -qF "$MARKER" ~/.bashrc; then
    # Append the script to ~/.bashrc
    echo "$SCRIPT" >> ~/.bashrc
    echo -e "${CONFIG} has been \033[1;32msuccessfully added to \033[1;33m~/.bashrc\033[0m."
else
    echo -e "${CONFIG}\033[1;31m already exists. \033[1;33mNo changes made. \033[0m."
fi