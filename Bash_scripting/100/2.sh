#!/bin/bash
# 2. Create two vars IP="10.0.0.1" and PORT=22. Echo "10.0.0.1:22".
#    (Use "${IP}:${PORT}" — the ${} braces are safer than bare $VAR)

IP="10.0.0.1"
PORT=22

echo $IP:$PORT
