#!/bin/bash
# 78. Find the largest number in numbers.txt (no sort).
#     awk 'NR==1 || $1 > max {max=$1} END {print max}' numbers.txt
awk 'NR==1 || $1 > max {max=$1} END {print max}' numbers.txt
