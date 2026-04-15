#!/bin/bash
# 45. awk 'END {print NR}' logs.txt  — count lines (prints total NR at end).

awk 'END {print NR}' logs.txt
