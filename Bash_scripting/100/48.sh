#!/bin/bash
# 48. awk '{print NR": "$0}' logs.txt  — print line number prefix (like nl).

awk '{print NR": "$0}' logs.txt
