#!/bin/bash
# 80. Process dict equivalent — given a file `processes.txt` with:
#     1234 45.2 nginx
#     1235 12.8 postgres
#     ...
#     Sum CPU column (col 2).
#     awk '{s += $2} END {print s}' processes.txt
 cat > processes.txt << 'EOF'
1234 45.2 nginx
1235 12.8 postgres
1236 78.5 nginx
1237 8.3 systemd
1238 92.1 python3
1239 34.6 postgres
1240 2.1 cron
1241 55.4 nginx
1242 18.9 redis-server
1243 67.2 python3
EOF

awk '{s += $2} END {print s}' processes.txt
