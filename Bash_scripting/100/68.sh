#!/bin/bash
# 68. Write a function `check_service` that takes a service name, runs
#     systemctl is-active, and echoes "OK" or "DOWN".

check_service(){
    local svc="${1}"
    local service=$(systemctl --user is-active "${svc}")
    if [ "${service}" = "active" ]; then
        echo "OK"
    else
        echo "DOWN"
    fi
}

check_service wallpaper.service
check_service no_service
