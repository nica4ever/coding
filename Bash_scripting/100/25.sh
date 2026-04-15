#!/bin/bash
# 25. Read logs.txt line by line. Print only lines containing "ERROR".
#     (Don't use grep yet — do it with if and case or [[ "$line" == *ERROR* ]])

while read -r line; do
    if [[ ${line} == *ERROR* ]]; then
        echo "${line}"
    fi
done < logs.txt
