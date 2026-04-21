#!/bin/bash
# 63. Write a function `is_even` that takes a number and echoes "even" or "odd".

is_even(){
    if [ $(($1%2)) -eq 0 ]; then
        echo "even"
    else
        echo "odd"
    fi
}

is_even 1
is_even 2
