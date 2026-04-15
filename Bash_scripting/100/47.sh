#!/bin/bash
# 47. awk '{sum += $4} END {print sum}' numbers.txt  — numeric sum of a field.
#     (For numbers.txt, $1 is the number itself. Use $1.)

awk '{sum += $1} END {print sum}' numbers.txt
