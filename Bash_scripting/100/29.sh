#!/bin/bash
# 29. Check if a file exists before reading it:
#     if [ -f "logs.txt" ]; then cat logs.txt; else echo "not found"; fi

if [ -f "logs.txt" ]; then
    cat logs.txt
else
    echo "not found"
fi
