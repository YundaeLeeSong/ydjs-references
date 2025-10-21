#!/bin/bash
############################################
################# Variable #################
############################################
# constants for directory paths
readonly JAVA="./ext"
readonly JLIB="./lib"
# system related variables
export JAVA_HOME="$(pwd)/${JAVA}/jdk-11.0.2"                # Java Language System (JDK)
export KOTLIN_HOME="$(pwd)/${JAVA}/kotlinc"                 # Kotlin Language System
export ANT_HOME="$(pwd)/${JAVA}/apache-ant-1.10.14"         # Apache Ant - Java Build Automation








############################################
####### Internal (Private) Functions #######
############################################
_set_path() {
    local directory="$1"
    export PATH="$directory:$PATH"
}
_dependency() {
    echo $'\n\n****************************************\n'  
    echo $'*********** checking your dependency now...\n'
    echo $'****************************************\n'
    java -version
    echo $'\t^^^^^ <java>\n'
    kotlinc -version
    echo $'\t^^^^^ <kotlinc>\n'
    ant -version
    echo $'\t^^^^^ <ant>\n'
}
_complie() {
    echo $'\n\n****************************************\n'  
    echo $'*********** compiling your program now...\n'
    echo $'****************************************\n'
    ant compile
    echo $'\n\n****************************************\n'  
    echo $'*********** archiving your program now...\n'
    echo $'****************************************\n'
    ant archive
}
_run() {
    echo $'\n\n****************************************\n'
    echo $'*********** running your program now...\n'
    echo $'****************************************\n'
    ant run
}
_clean() {
    echo $'\n\n****************************************\n'
    echo $'*********** cleaning build configuration files now...\n'
    echo $'****************************************\n'
    ant clean
    # read -p $'\n\n\tDo you want to clean your build configuration files? (Y/N)' user_input
    # if [ "$(echo "${user_input}" | tr '[:upper:]' '[:lower:]')" == "y" ]; then
    #     ant clean                                       # To clean the build artifacts
    #     echo $'\tBuild configuration files have been cleaned..'
    #     read -n 1 -p $'\tPress any key to run your application...' 
    # fi
}



############################################
########## Shell Script (Scripts) ##########
############################################
PACKAGE_NAME=$(basename "$(pwd)") # base name of the current directory
main() {
    #### path setup
    _set_path "${JAVA_HOME}/bin"
    _set_path "${KOTLIN_HOME}/bin"
    _set_path "${ANT_HOME}/bin"

    #### scripts
    _dependency
    _complie
    # _run
    # _clean


    ########################################
    ########## manual compilation ##########
    ########################################
    # ######### 01. Compilation
    # javac -d lib/classes -cp "lib/db-derby-10.14.2.0-bin/lib/derby.jar" src/*.java
    # ########## 02. Archive (deployment)
    # #### MANIFEST.MF relative to jar.*
    # jar cfm "lib/$PACKAGE_NAME.jar" META-INF/MANIFEST.MF -C build/classes . 
    # ########## 03. Run
    # java --module-path lib/javafx-sdk-11.0.2/lib --add-modules javafx.controls -jar "lib/$PACKAGE_NAME.jar" 
    # ########## 99. Clean
    # rm -rf build
    # rm -rf res/db
    # rm -f derby.log
    # echo "Clean target completed."


    ########################################
    ########## cs3312 production ##########
    ########################################
    # ########## 03. Run
    #### jar execution relative to user's root direcotry.
    java --module-path lib/javafx-sdk-11.0.2/lib --add-modules javafx.controls -jar "dist/$PACKAGE_NAME.jar"
    rm -rf build
    rm -rf res/db
    rm -f derby.log
    echo "Clean target completed."
}



############################################
############ Executable Script #############
############################################
echo -e "..............................."
echo -e "Start build process......"
echo -e "..............................."
main

##############################< documentation >##################################
# 01) ./                execute a "new session" of shell environment)
# 02) source            import within "current session" of shell environment)
# 03) $'...'            ansi c quoting syntax
# 04) rm -rf            "R"e"M"ove files or directories "R"ecursively and "F"orcefully
# 05) read -n 1 -p      "READ" 1 "N"umber of characters with "P"rompt
# 06) echo -e           enable "E"scape characters
# 07) 
# 08) 
# 09) 
# 10) 
# 11) 
# 12) 
# 13) 
#################################################################################

##############################< jar documentation >##################################
# 01) -c: create a Java ARchive (JAR)
# 02) -f: filename the JAR
# 03) -m: manifest file to include in the JAR
# 04) -C: change directory
# 05) (.): all class files and in the directory recursively
# 06) 
# 07) 
# 08) 
# 09) 
# 10) 
# 11) 
#################################################################################