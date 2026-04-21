#!/bin/bash
# 59. sort logs.txt | uniq -c | sort -rn  — sorted by count descending. (THE classic pipeline.)
sort logs.txt | uniq -c | sort -rn
