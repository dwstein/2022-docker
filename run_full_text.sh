#!/bin/bash

# File where all text will be accumulated
output_file="full_text.txt"
# Ensure the output file is empty initially by overwriting it
: > "$output_file"

# Traverse directories, find specific files, and ignore __pycache__ directories
find . -type f \( -name "*.py" -o -name "Dockerfile" -o -name "*.yaml" -o -name "README.md" -o -name "requirements.txt" \) ! -name "run_full_text.sh" ! -name "$output_file" \
-exec sh -c 'cat "$1" >> "$2" && echo "" >> "$2"' _ {} "$output_file" \;

# Append the directory tree to the output file, ignoring __pycache__ directories
# echo "Directory Tree:" >> "$output_file"
# tree -I '__pycache__' >> "$output_file"
