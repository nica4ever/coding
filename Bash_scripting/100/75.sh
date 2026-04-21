#!/bin/bash
# 75. From access.log, count 4xx errors:
#     awk '$4 >= 400 && $4 < 500' access.log | wc -l

awk '$4 >= 400 && $4 < 500' acess.log | wc -l
