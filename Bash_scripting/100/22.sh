#!/bin/bash 
# 22. Same loop but with an index counter:
#     i=0
#     while read -r line; do echo "$i: $line"; i=$((i + 1)); done < servers.txt

i=0

while read -r line;
do echo "${i}: ${line}"; i=$((i + 1));
done < servers.txt
