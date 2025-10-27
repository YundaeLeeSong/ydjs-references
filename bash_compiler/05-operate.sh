#!/bin/bash

# Declare an array (list) with initial values
my_list=("apple" "banana" "cherry" "date")

# Adding an element to the array
my_list+=("elderberry")

# Accessing elements of the array
echo "Array: ${my_list}"
echo "First element: ${my_list[0]}"
echo "Second element: ${my_list[1]}"

# Getting the length of the array
length=${#my_list[@]}
echo "The list has $length elements."

# Looping through the array elements
echo "All elements in the list:"
for item in "${my_list[@]}"; do
    echo "$item"
done

# Removing the last element from the array
unset my_list[-1]

# Print the modified array
echo "Modified list after removing the last element:"
for item in "${my_list[@]}"; do
    echo "$item"
done








# Use globbing to get all subdirectories in the current directory
subdirs=(*/)

# Echo the list as it is (removing trailing slashes)
echo "Subdirectories: ${subdirs[@]%/}"

# Iterate through the list and echo each element (removing trailing slashes)
echo "Iterating through the list:"
for dir in "${subdirs[@]}"; do
    echo "${dir%/}"
done







# Semicolon-separated string
my_string="item1;item2;item3"

# Convert to array by splitting on semicolons
IFS=';' read -r -a my_array <<< "$my_string"

# Iterate over the array
echo ""
echo "Array String itself: ${my_string}"    
echo "Array itself: ${my_array}"
echo "Array elements: ${my_array[@]}"       # Print as array (space-separated by default)
echo "Array elements in loop: "
for item in "${my_array[@]}"; do
    echo "$item"
done