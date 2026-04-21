#!/bin/bash
# 73. Same but sorted by count descending.

grep "ERROR" logs.txt | awk '{print $4}' | sort -r | uniq  

