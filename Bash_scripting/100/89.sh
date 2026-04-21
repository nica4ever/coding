#!/bin/bash
# 89. Parse /etc/passwd. Return all usernames with UID >= 1000 (real users).
#     awk -F':' '$3 >= 1000 {print $1}' /etc/passwd
awk -F':' '$3 >= 1000 {print $1}' /etc/passwd
