#!/bin/bash

tree
echo ""

file_list=("app.py" "templates/index.html" "static/script.js")

for file in "${file_list[@]}"; do
    echo "=== Contents of $file ==="
    cat "$file"
    echo ""
done
