#!/bin/bash
# 77. Total of all numbers in numbers.txt using awk.
#     awk '{s += $1} END {print s}' numbers.txt
awk '{s += $1} END {print s}' numbers.txt
