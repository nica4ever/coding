#!/bin/bash
# 54. sort -r logs.txt  — reverse sort.

awk '{print $4}' logs.txt | sort -r

