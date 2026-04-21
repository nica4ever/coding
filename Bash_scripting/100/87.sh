#!/bin/bash
# 87. Write a function `in_time_window` that takes a logfile, start_time, end_time
#     and outputs all lines whose timestamp falls within that window.

in_time_window(){
    local log="${1}"
    awk -v min="${2}" -v max="${3}" '$2 >= min && $2 <= max {print}' "${log}"
}

in_time_window "${1}" "${2}" "${3}"
