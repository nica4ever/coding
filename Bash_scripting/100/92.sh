#!/bin/bash
# 92. Show all running processes using more than X% CPU (X is argument).
#     ps aux | awk -v x=$1 '$3 > x {print $0}'
ps aux | awk -v x="${1}" '$3 > x {print $0}'
