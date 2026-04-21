#!/bin/bash
# 85. Find logs between two timestamps (string comparison works for ISO format):
#     awk '$1" "$2 >= "2024-03-15 10:00:10" && $1" "$2 <= "2024-03-15 10:00:30"' logs.txt
awk '$1" "$2 >= "2024-03-15 10:00:10" && $1" "$2 <= "2024-03-15 10:00:30"' logs.txt 
