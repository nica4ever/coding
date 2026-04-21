#!/bin/bash
# 83. Same but sorted by total CPU descending:
#     awk '{cpu[$3] += $2} END {for (name in cpu) print cpu[name], name}' processes.txt | sort -rn
awk '{cpu[$3] += $2} END {for (name in cpu) print cpu[name], name}' processes.txt | sort -r
