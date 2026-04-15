#!/bin/bash
# 27. Count how many lines in logs.txt contain "ERROR" — track with a variable, increment with ((count++))

count=0

while read -r date time level service message; do
    if [ "${level}" == "ERROR" ]; then
        ((count++))
    fi
done < logs.txt

echo "$count"

