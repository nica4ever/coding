#!/bin/bash
# 84. Count requests per minute from a log file (extract HH:MM from timestamps).
#     awk '{split($2, t, ":"); print t[1]":"t[2]}' logs.txt | sort | uniq -c
awk '{split($2, t, ":"); print t[1]":"t[2]}' logs.txt | sort | uniq -c
