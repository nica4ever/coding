#!/bin/bash
# 28. If total lines in logs.txt is greater than 5, echo "Long log". Otherwise "Short log".
#     (Use wc -l with command substitution: TOTAL=$(wc -l < logs.txt))

TOTAL=$(wc -l < logs.txt)

if [ "${TOTAL}" -gt 5 ]; then
    echo "Long log"
else
    echo "Short log"
fi
