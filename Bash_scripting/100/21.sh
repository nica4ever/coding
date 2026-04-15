#!/bin/bash
# 21. Loop through servers.txt and echo each name.
#     while read -r line; do echo "Server: $line"; done < servers.txt

cat > servers.txt << 'EOF'
web-01
db-01
cache-01
worker-01
lb-01
EOF

while read -r line;
do echo "Server: ${line}"
done < servers.txt
