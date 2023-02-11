#!/bin/bash

# type bash test_bash.sh to run
# No spaces between assignments

echo "Checking for duplicates..."

# Path
path="/c/Users/Corey/Documents/Projects"
directory="dummy"
cwd="$path/$directory"
files="*.md"  # Does not work with README

# Command to search files
echo "find $cwd -name $files"
echo "Searching for $files..."
# find $cwd -name $files
# find $cwd -name $files -not -empty -type f -printf "%f\n"

# Using a loop to search files in directory
for f in $cwd/*  # Added /* to print inside directory, not just the directory itself
do
    # f="${f##*/}"   # strip path and leading slash
    echo
    echo "Found file in $f"
    echo "Created:" $(stat -c %w $f)
    echo "Last Accessed:" $(stat -c %x $f)
    echo "Last Modified:" $(stat -c %y $f)
    echo "Last Status Changed:" $(stat -c %z $f)
done

# > dups.txt
# | uniq -d

# File creation
# stat "$cwd/README.md"

# Test
# echo -e "Please enter your name: "
# read name
# echo "Nice to meet you $name"
