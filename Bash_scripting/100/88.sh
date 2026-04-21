#!/bin/bash
# 88. Write a function `suspicious_ips` that finds IPs in access.log
#     that made more than N failed requests (4xx/5xx). N is an argument.

supicious_ip(){
    local log="${1}"
    local N="${2}"
    awk '$4 >= 400 && $4 < 600 {print $1}' "${log}" | sort | uniq -c | sed 's/^ *//' | awk -v range="${N}" '$1 > range {print}'
}

supicious_ip "${1}" "${2}"
