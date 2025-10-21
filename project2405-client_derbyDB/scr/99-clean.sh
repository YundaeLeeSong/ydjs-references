echo $'\n\n****************************************\n'
echo $'*********** cleaning build configuration files now...\n'
echo $'****************************************\n'
# read -p $'\n\n\tDo you want to clean your build configuration files? (Y/N)' user_input
# if [ "$(echo "${user_input}" | tr '[:upper:]' '[:lower:]')" == "y" ]; then
#     ant clean                                       # To clean the build artifacts
#     echo $'\tBuild configuration files have been cleaned..'
#     read -n 1 -p $'\tPress any key to run your application...' 
# fi
ant clean                                       # To clean the build artifacts
##############################< documentation >##################################
# 01) $'...'            ansi c quoting syntax
# 02) rm -rf            "R"e"M"ove files or directories "R"ecursively and "F"orcefully
# 03) read -n 1 -p      "READ" 1 "N"umber of characters with "P"rompt
# 04) 
# 05) 
# 06) 
# 07) 
# 08) 
# 09) 
# 10) 
# 11) 
#################################################################################