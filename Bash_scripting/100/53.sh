#!/bin/bash
# 53. sort logs.txt  — alphabetical sort.

awk '{print $4}' logs.txt | sort
