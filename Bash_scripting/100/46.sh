#!/bin/bash
# 46. awk '/ERROR/ {count++} END {print count}' logs.txt  — count lines matching pattern.
 awk '/ERROR/ {count++} END {print count}' logs.txt
