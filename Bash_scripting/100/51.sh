#!/bin/bash
# 51. sed '/^$/d' somefile.txt  — delete blank lines.

cat > somefile.txt << 'EOF'
Line

Line


Line

Line

EOF

sed '/^$/d' somefile.txt
