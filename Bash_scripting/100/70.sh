#!/bin/bash
# 70. Function with default argument:
#     top_n() {
#         local file="$1"
#         local n="${2:-5}"   # default 5 if $2 not provided
#         awk '{print $1}' "$file" | sort | uniq -c | sort -rn | head -n "$n"
#     }

top_n(){
    local file="${1}"
    local n="${2:-5}"
    awk '{print $1}' "${file}" | sort | uniq -c | sort -rn | head -n "${n}"
}

top_n logs.txt
