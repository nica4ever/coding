#!/bin/bash
# 66. Write a function `top_ip` that takes an access log file and echoes
#     the most frequent IP. Use awk + sort + uniq + head.

top_ip(){
    awk '{print $1}' "${1}" | sort -n | uniq -c | head -n1
}

top_ip acess.log
