#!/bin/bash
# 74. From access.log, find the top 3 most frequent IPs:
#     awk '{print $1}' access.log | sort | uniq -c | sort -rn | head -n 3

awk '{print $1}' acess.log | sort | uniq -c | sort -rn | head -n 3
