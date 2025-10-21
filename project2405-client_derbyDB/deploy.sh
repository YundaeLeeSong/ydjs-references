#!/bin/bash
############################################
################# Variable #################
############################################
# constants
readonly JAVA="./ext"
readonly JLIB="./lib"
# system related variables
export JAVA_HOME="$(pwd)/${JAVA}/jdk-11.0.2"                # Java Language System (JDK)
export KOTLIN_HOME="$(pwd)/${JAVA}/kotlinc"                 # Kotlin Language System
export ANT_HOME="$(pwd)/${JAVA}/apache-ant-1.10.14"         # Apache Ant - Java Build Automation
# project related variables
KOT="${JLIB}/kotlin-stdlib-1.6.10"                          # Kotlin Runtime Environment (KRE)
JFX="${JLIB}/javafx-sdk-11.0.2/lib"                         # JavaFX framework                  - graphical UI
JDB1="${JLIB}/db-derby-10.14.2.0-bin/lib"                   # JDBC Apache Derby                 - database
JDB2="${JLIB}/ojdbc-11"                                     # JDBC Oracle                       - database

############################################
################## Functions ################
############################################
install() {
    os_type=$(uname)
    case "$os_type" in
        "Linux"*) 
            # Linux operating system
            echo "Start installing, your operating system type: $os_type"
            source ./scr/00-install-linux.sh
            ;;
        "Darwin"*)
            # macOS
            echo "Start installing, your operating system type: $os_type"
            echo "The current machine is running macOS."
            echo "No actions will be taken."
            ;;
        "CYGWIN"*|"MINGW32"*|"MSYS"*|"MINGW"*)
            # Windows-like operating system
            echo "Start installing, your operating system type: $os_type"
            source ./scr/00-install-win.sh
            ;;
        *)
            echo "Unable to determine the operating system type: $os_type"
            ;;
    esac
}
config() {
    sed -i '0,/grant codeBase/ { s//grant { permission java.security.AllPermission; };\n\n&/ }' "$JAVA/jdk-11.0.2/lib/security/default.policy"
}
validate_directory() {
    local directory="$1"
    if [ -d "$directory" ]; then
        echo -e "\033[0;32m$directory (ready)\033[0m"
    else
        echo -e "\033[0;31m$directory (missing)\033[0m"
    fi
}

############################################
########## Shell Script (Scripts) ##########
############################################
main() {
    ## Dependency Installation: Install required libraries, modules, or dependencies.
    install
    ## Environment and Config Setup: settings for the production environment and its configurations.
    config
    ## Post-Deployment Verification: Verify that the deployment was successful
    echo -e "\n\n< Java >"
    # system related deployment
    validate_directory "${JAVA_HOME}"
    validate_directory "${ANT_HOME}"
    validate_directory "${KOTLIN_HOME}"
    # project related deployment
    validate_directory "$(pwd)/${KOT}"
    validate_directory "$(pwd)/${JFX}"
    validate_directory "$(pwd)/${JDB1}"
    validate_directory "$(pwd)/${JDB2}"
    ####################################################################################################
    ## (future ref) Database Migrations, User Notifications, Update Documentation, Server Restart/Reload
    ####################################################################################################
}

main
## Build (build.sh): Compile the code and assets (stylesheets and scripts), then execute it.
# build commands