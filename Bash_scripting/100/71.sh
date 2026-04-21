#!/bin/bash
# 71. From logs.txt, return only ERROR lines, sorted by timestamp.
#     Pipeline: grep ERROR | sort

grep "ERROR"  logs.txt | sort -k2
