#!/bin/bash
# 76. From access.log, percentage of 5xx errors.
#     TOTAL=$(wc -l < access.log)
#     ERRORS=$(awk '$4 >= 500 && $4 < 600' access.log | wc -l)
#     echo "scale=2; $ERRORS * 100 / $TOTAL" | bc

TOTAL=$(wc -l < acess.log)
ERRORS=$(awk '$4 >= 500 && $4 < 600' acess.log | wc -l)
echo "scale=2; ${ERRORS} * 100 / ${TOTAL}" | bc
