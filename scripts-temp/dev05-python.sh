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

TITLE="Python Language System (PVM)"
CONFIG="General configuration for '${TITLE}'" # configuration title
MARKER="?PYTHON;" # Check if the configuration script exists in ~/.bashrc
SCRIPT=$(cat <<'EOF'

###############################################################################
#                                   ?PYTHON;
################################################################################
# PVM="/Python312"                    # Python interpreter (Virtual Machine)
# TKI="/Python312/libs"               # tkinter (TK graphical user Interface)
# PXE="/Python312/Scripts"            # Python eXecutablE scripts, e.g. pip (dependency management)
# PIL="/Python312/Lib"                # Python Internal Library (standard)
# PXL="/Python312/Lib/site-packages"  # Python External Library (3rd party packages)
#################################< VERSION >####################################
PYTHON_VERSIONS=("3.8.10" "3.9.13" "3.10.11" "3.11.2" "3.12.2")
PYTHON_VERSIONS=("3.10.11" "3.11.2" "3.12.2")
PYTHON_VERSIONS=("3.12.2")
##################################< USAGE >#####################################
# ### language system setup ... (1)
# enable_python
###############################################################################
PYTHON_URL="https://www.python.org/ftp/python/{VERSION}/python-{VERSION}-embed-amd64.zip"
PYTHON_DIR="${PROJ_EXT}/Python{VERSION}"
function enable_python {
    # PVM checkup (positive)
    if exists "$PROJ_EXT" "Python"; then
        echo "Notice: Directory $(USRPROMPT ''${PYTHON_DIR}' ')already exists. PVE has been setup..."
        # PVE setup
        SETUP_PYTHON
        return
    fi
    # PVM install
    for ver in "${PYTHON_VERSIONS[@]}"; do
        url="${PYTHON_URL//\{VERSION\}/$ver}"
        echo $url
        ver=$(echo "$ver" | awk -F. '{print $1 $2}')                                        # version modification e.g. "3.12.2" to "312"
        INSTRACT "$url" "python.zip" "${PROJ_EXT}/Python$ver"
        echo -e "python$ver.zip\n.\nimport site" > "$PROJ_EXT/Python$ver/python$ver._pth"   # enable `Lib/site-packages`
        curl -o "${PROJ_EXT}/get-pip.py" "https://bootstrap.pypa.io/get-pip.py"             # PIP script
        ${PYTHON_DIR//\{VERSION\}/$ver}/python "${PROJ_EXT}/get-pip.py"         # Package Installer for Python
        rm "${PROJ_EXT}/get-pip.py"                                                         # clean PIP script
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install tox                             # test automation (by virtualenv) 
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install poetry                          # [1] build automation (by virtualenv, setuptools) 
        ${PYTHON_DIR//\{VERSION\}/$ver}/Scripts/pip install pipreqs
    done
    # PVM checkup (negative)
    if [[ ! -d "$PROJ_EXT" ]]; then
        echo "Error: $(TEST_FAIL 'There is no '${PROJ_EXT}' found.')"
        return
    fi
    # PVE setup
    SETUP_PYTHON
}
function SETUP_PYTHON {
    for ver in "${PYTHON_VERSIONS[@]}"; do
        ver=$(echo "$ver" | awk -F. '{print $1 $2}')    # version modification e.g. "3.12.2" to "312"
        export PATH="${PYTHON_DIR//\{VERSION\}/$ver}:${PATH}"
        export PATH="${PYTHON_DIR//\{VERSION\}/$ver}/Scripts:${PATH}"
    done
    python --version
    pip --version
    poetry --version
    tox --version
    pipreqs --version
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