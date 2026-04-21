#!/bin/bash
# 69. Functions returning values: in bash, "return" sets exit code (0-255 only).
#     For actual values, echo the result and capture with command substitution:
#     result=$(my_function arg1)
#     Write a function `count_lines` that takes a file and "returns" line count.

lines(){
    [ -f "${1}" ] || return 1
    wc -l < "${1}"
    
}


if result=$(lines logs.txt); then 
    echo "Lines: ${result}"
else
    echo "Failed: file not found"
    exit 1
fi
