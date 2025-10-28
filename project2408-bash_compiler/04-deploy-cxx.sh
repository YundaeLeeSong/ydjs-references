#!/bin/bash



# Function to list files with custom delimiter
lstr() {
  local glob_pattern="$1"
  local delimiter="$2"

  # Use eval to perform globbing and list files
  local files=$(eval "ls ${glob_pattern}")

  # Use for loop to convert each file to absolute path
  local result=""
  for file in $files; do
    result+=$(realpath "$file")$delimiter
  done

  # Remove the trailing delimiter (optional)
  echo "${result%"${delimiter}"}"
}

# Function to find files with custom delimiter
findtr() {
  local find_pattern="$1"
  local delimiter=$2

  # Use eval to perform find and list files
  local files=$(eval "find $find_pattern")

  # Use for loop to convert each file to absolute path
  local result=""
  for file in $files; do
    result+=$(realpath "$file")$delimiter
  done

  # Remove the trailing delimiter (optional)
  echo "${result%"$delimiter"}"
}







# Create the directory structure
mkdir -p ./project/data
mkdir -p ./project/scripts
mkdir -p ./project/images

# Create some files with corrected names
touch ./project/data/file-1.txt
touch ./project/data/file-2.txt
touch ./project/data/file-3.csv
touch ./project/data/file-7.txt
touch ./project/data/file-99.txt
touch ./project/data/script-10.sh
touch ./project/data/script-20.sh
touch ./project/scripts/script-1.sh
touch ./project/scripts/script-2.sh
touch ./project/images/image-1.jpg
touch ./project/images/image-2.png
touch ./project/README.md
touch ./project/setup.sh

# List all files and directories in ./project
all_files_and_dirs=$(findtr "./project -mindepth 1 -maxdepth 1" ';')
echo "1. List all files and directories in ./project:"
echo "$all_files_and_dirs"

# List all .txt files in ./project/data
txt_files=$(lstr "./project/data/*.txt" ';')
echo -e "\n2. List all .txt files in ./project/data:"
echo "$txt_files"
# $(realpath "$...")
# List files in ./project/data with a single digit in their name
single_digit_files=$(lstr "./project/data/file-?.txt" ';')
echo -e "\n3. List files in ./project/data with a single digit in their name:"
echo "$single_digit_files"

# List files in ./project/data with either 1 or 2 in their name
one_or_two_files=$(lstr "./project/data/file-[12].txt" ';')
echo -e "\n4. List files in ./project/data with either 1 or 2 in their name:"
echo "$one_or_two_files"

# List .sh files in both ./project/scripts and ./project/data using `lstr`
sh_files=$(lstr "./project/{data,scripts}/*.sh" ';')
echo -e "\n5. List .sh files in both ./project/scripts and ./project/data:"
echo "$sh_files"

# List .jpg and .png files in ./project/images using `lstr`
image_files=$(lstr "./project/images/*.{jpg,png}" ';')
echo -e "\n6. List .jpg and .png files in ./project/images:"
echo "$image_files"

# List all .txt files in ./project and its subdirectories using `findtr`
txt_files_recursive=$(findtr "./project -type f -name '*.txt'" ';')
echo -e "\n7. List all .txt files in ./project and its subdirectories:"
echo "$txt_files_recursive"

# Clean up (optional)
rm -r ./project