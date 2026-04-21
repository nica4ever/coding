#!/bin/bash
# 90. From /proc/meminfo, print total memory in MB.
#     (MemTotal is in KB.) awk '/MemTotal/ {print $2/1024 " MB"}' /proc/meminfo
awk '/MemTotal/ {print $2/1024 " MB"}' /proc/meminfo
