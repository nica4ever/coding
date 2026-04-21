#!/bin/bash
# 86. Write a script that takes a log filename as $1 and prints:
#     - total lines
#     - error count
#     - warning count
#     - top 3 services by error count

# Count lines\
echo"Log lines:"
wc -l "${1}"
echo ""

# Count errors
echo "ERROR Lines:"
grep "ERROR" "${1}" | wc -l
echo ""

# Count warning
echo "WARNING Lines:"
grep "WARN" "${1}" | wc -l
echo ""

# Top 3 services by error count
echo "Top 3 services by error:"
awk '{if ($3 == "ERROR") {print $4} }' "${1}" | sort | uniq -c | sort -rn | head -n 3 | sed 's/^ *//'
