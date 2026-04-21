#!/bin/bash
# 60. awk '{print $3}' logs.txt | sort | uniq -c  — count unique log levels.
 awk '{print $3}' logs.txt | sort | uniq -c
