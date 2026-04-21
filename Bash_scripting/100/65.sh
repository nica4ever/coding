#!/bin/bash
# 65. Write a function `count_errors` that takes a log filename and echoes
#     the number of ERROR lines in it. Use grep -c inside.

count_errors(){
    if [ -e "${1}" ]; then
        grep -c "ERROR" "${1}"
    else
        echo "File not found"
    fi
}

count_errors logs.txt
count_errors no_entry

