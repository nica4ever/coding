#!/bin/bash
# 72. From logs.txt, count errors per service. Output:
#     3 auth-service
#     1 cache-redis
#     1 payment-gateway
#     1 worker-queue
#     (Pipeline: grep ERROR | awk '{print $4}' | sort | uniq -c)

grep "ERROR" logs.txt | awk '{print $4}' | sort | uniq -c
