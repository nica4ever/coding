#!/bin/bash
# 79. Count unique log levels in logs.txt.
#     awk '{print $3}' logs.txt | sort -u | wc -l
awk '{print $3}' logs.txt | sort -u | wc -l
