#!/bin/bash
# 24. Loop 1-20, print only even numbers. (Use if and the % operator)

for i in $(seq 1 20);
do if [[ $((i % 2)) -eq 0 ]]; then
        echo "${i}"
    fi
done
