#!/bin/bash
# 91. Generate a report of disk usage on all mounted filesystems,
#     flagging any above 80% usage.
#     df -h | awk 'NR>1 && int($5) > 80 {print $6 " is at " $5}'
df -h | awk 'NR>1 && int($5) > 80 {print $6 " is at " $5}'
