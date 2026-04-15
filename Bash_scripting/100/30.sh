#!/bin/bash
# 30. Check if a directory exists:
#     if [ -d "/var/log" ]; then echo "yes"; else echo "no"; fi

if [ -d "/var/log" ]; then
    echo "yes"
else
    echo "no:"
fi
