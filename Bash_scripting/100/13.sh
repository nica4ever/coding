#!/bin/bash
# 13. Create a file `logs.txt` with the following lines (use a heredoc):
#     cat > logs.txt <<'EOF'
#     2024-03-15 10:00:01 INFO auth-service Started
#     2024-03-15 10:00:05 ERROR payment-gateway Transaction declined
#     2024-03-15 10:00:08 WARN db-primary Slow query
#     2024-03-15 10:00:12 INFO api-server Request OK
#     2024-03-15 10:00:18 ERROR auth-service Connection refused
#     2024-03-15 10:00:22 INFO worker-queue Job completed
#     2024-03-15 10:00:30 ERROR cache-redis Cache miss
#     2024-03-15 10:00:35 WARN load-balancer High latency
#     2024-03-15 10:00:40 INFO db-replica Replication OK
#     2024-03-15 10:00:45 ERROR worker-queue Task failed
#     EOF

cat > logs.txt << 'EOF'
2024-03-15 10:00:01 INFO auth-service Started
2024-03-15 10:00:05 ERROR payment-gateway Transaction declined
2024-03-15 10:00:08 WARN db-primary Slow query
2024-03-15 10:00:12 INFO api-server Request OK
2024-03-15 10:00:18 ERROR auth-service Connection refused
2024-03-15 10:00:22 INFO worker-queue Job completed
2024-03-15 10:00:30 ERROR cache-redis Cache miss
2024-03-15 10:00:35 WARN load-balancer High latency
2024-03-15 10:00:40 INFO db-replica Replication OK
2024-03-15 10:00:45 ERROR worker-queue Task failed
EOF
