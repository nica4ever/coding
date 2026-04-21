#!/bin/bash
# 93. From a Nginx access log, return top 10 URLs by request count.
#     awk '{print $7}' access.log | sort | uniq -c | sort -rn | head -n 10
awk '{print $7}' acess.log | sort | uniq -c | sort -rn | head -n 10
