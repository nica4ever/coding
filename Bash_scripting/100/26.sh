#!/bin/bash
# 26. Same thing, but only print lines where the service is "auth-service".
#     (Hint: use awk or parse fields manually)

awk '$4 == "auth-service" {print}' logs.txt
