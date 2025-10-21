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

TITLE="Java Development Kit (JDK)"
CONFIG="General configuration for '${TITLE}'" # configuration title
MARKER="?JAVA;" # Check if the configuration script exists in ~/.bashrc
SCRIPT=$(cat <<'EOF'

###############################################################################
#                                   ?JAVA;
################################################################################
#################################< VERSION >####################################
JDK_VERSIONS=("21" "17")
JDK_IDENTIFIERS=("fd2272bbf8e04c3dbaee13770090416c" "0d483333a00540d886896bac774ff48b")
GRADLE_VERSIONS=("8.5" "7.3")

JDK_VERSIONS=("17")
JDK_IDENTIFIERS=("0d483333a00540d886896bac774ff48b")
GRADLE_VERSIONS=("8.5")
##################################< USAGE >#####################################
# ### language system setup ... (1)
# enable_java
# ### build automation setup ... (2 requires `1`)
# enable_gradle
###############################################################################
JDK_URL="https://download.java.net/java/GA/jdk{VERSION}/{IDENTIFIER}/35/GPL/openjdk-{VERSION}_windows-x64_bin.zip"
JDK_DIR="${PROJ_EXT}/jdk-{VERSION}/bin"
function enable_java {
    # JDK checkup (positive)
    if exists "$PROJ_EXT" "jdk"; then
        echo "Notice: Directory $(USRPROMPT ''${JDK_DIR}' ')already exists. JRE/JVM has been setup..."
        # JRE/JVM setup
        SETUP_JAVA
        return
    fi
    # JDK install
    for i in "${!JDK_VERSIONS[@]}"; do
        ver="${JDK_VERSIONS[$i]}"
        identifier="${JDK_IDENTIFIERS[$i]}"
        url="${JDK_URL//\{VERSION\}/$ver}"
        url="${url//\{IDENTIFIER\}/$identifier}"
        INSTRACT "$url" "jdk.zip" "${PROJ_EXT}"
    done
    # JRE/JVM setup
    SETUP_JAVA
}
function SETUP_JAVA {
    for ver in "${JDK_VERSIONS[@]}"; do
        export JAVA_HOME="${PROJ_EXT}/jdk-${ver}"
        export PATH="${JDK_DIR//\{VERSION\}/$ver}:${PATH}"
    done
    echo -e "\n------------------------------------------------------------"
    echo -e "JAVA"
    echo -e "------------------------------------------------------------\n"
    java -version
    echo "JAVA_HOME: $JAVA_HOME"
    echo -e "------------------------------------------------------------\n"
}
GRADLE_URL="https://services.gradle.org/distributions/gradle-{VERSION}-bin.zip"
GRADLE_DIR="${PROJ_EXT}/gradle-{VERSION}/bin"
function enable_gradle {
    # Gradle checkup (positive)
    if exists "$PROJ_EXT" "gradle"; then
        echo "Notice: Directory $(USRPROMPT ''${GRADLE_DIR}' ')already exists. Gradle has been setup..."
        # Gradle setup
        SETUP_GRADLE
        return
    fi
    # Gradle install
    for ver in "${GRADLE_VERSIONS[@]}"; do
        url="${GRADLE_URL//\{VERSION\}/$ver}"
        INSTRACT "$url" "gradle.zip" "${PROJ_EXT}"
    done
    # Gradle setup
    SETUP_GRADLE
}
function SETUP_GRADLE {
    for ver in "${GRADLE_VERSIONS[@]}"; do
        export PATH="${GRADLE_DIR//\{VERSION\}/$ver}:${PATH}"
    done
    gradle -v
    echo -e "------------------------------------------------------------\n"
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