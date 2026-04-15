#!/bin/bash
# 15. Create `status_codes.txt` with one status code per line (many duplicates):
#     200, 404, 500, 200, 200, 404, 200, 301, 500, 200, 404, 503, 200, 502
#     (One per line. Use echo or a heredoc.)

cat > status_codes.txt << 'EOF'
200
404
500
200
200
404
200
301
500
200
404
503
200
502
EOF
