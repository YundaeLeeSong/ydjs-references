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






############################################
################## Functions ###############
############################################
add_path_directory() {
    local directory="$1"
    export PATH="$directory:$PATH"
}

############################################
########## Shell Script (Scripts) ##########
############################################
PACKAGE_NAME=$(basename "$(pwd)") # base name of the current directory
main() {
    #### path setup
    add_path_directory "${JAVA_HOME}/bin"
    add_path_directory "${KOTLIN_HOME}/bin"
    add_path_directory "${ANT_HOME}/bin"

    #### scripts
    source ./scr/01-dependency.sh
    source ./scr/02-complie.sh
    # source ./scr/03-run.sh
    # source ./scr/99-clean.sh


    ########################################
    ########## manual compilation ##########
    ########################################
    # ######### 01. Compilation
    # javac -d lib/classes -cp "lib/db-derby-10.14.2.0-bin/lib/derby.jar" src/*.java
    # ########## 02. Archive (deployment)
    # jar cfm "lib/$PACKAGE_NAME.jar" META-INF/MANIFEST.MF -C build/classes . # MANIFEST.MF relative to jar.*
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
    # # ########## 03. Run
    java --module-path lib/javafx-sdk-11.0.2/lib --add-modules javafx.controls -jar "$PACKAGE_NAME.jar" # jar execution relative to root direcotry.*
    rm -rf build
    rm -rf res/db
    rm -f derby.log
    echo "Clean target completed."
}

main

##############################< documentation >##################################
# 01) ./                execute a "new session" of shell environment)
# 02) source            import within "current session" of shell environment)
# 03) 
# 04) 
# 05) 
# 06) 
# 07) 
# 08) 
# 09) 
# 10) 
# 11) 
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