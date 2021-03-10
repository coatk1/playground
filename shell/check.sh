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
for f in $cwd/*  # Added /* to print inside directory, not just the directory itself
do
    f="${f##*/}"   # strip path and leading slash
    echo "$f"
    # cat $f
done

# > dups.txt
# | uniq -d

# File creation
# stat "$cwd/README.md"

# Test
# echo -e "Please enter your name: "
# read name
# echo "Nice to meet you $name"
