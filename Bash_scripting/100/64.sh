#!/bin/bash
# 64. Write a function `file_exists` that takes a filename. If the file exists,
#     echo "found". If not, echo "missing".

file_exists(){
    if [ -e "${1}" ]; then
        echo "found"
    else
        echo "Not found"
    fi
}

file_exists logs.txt
file_exists no_entry.txt
