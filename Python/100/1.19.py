# 1.19 Create three variables: level="ERROR", service="auth", msg="timeout"
#      Print them in this exact format: [ERROR   ] auth         timeout
#      Use f-string padding to align columns.
level = "ERROR"
service = "auth"
msg = "timeout"
print(f'[{level:<10}] {service} {msg:>10}')
