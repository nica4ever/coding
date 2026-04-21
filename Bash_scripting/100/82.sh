#!/bin/bash
# 82. From processes.txt, group by name (col 3), sum CPU per group:
#     awk '{cpu[$3] += $2} END {for (name in cpu) print name, cpu[name]}' processes.txt
awk '{cpu[$3] += $2} END {for (name in cpu) print name, cpu[name]}' processes.txt
