# 5.17 Given a list of 5 "IP METHOD PATH STATUS" strings,
#      parse each into a dict and store all dicts in a list.
#      Print the list.
requests = [
    "10.0.0.1 GET /index.html 200",
    "10.0.0.2 POST /api/login 401",
    "10.0.0.1 GET /style.css 200",
    "10.0.0.3 GET /admin 403",
    "10.0.0.2 POST /api/login 401",
]

def line_dic(requests):
    result = []                          
    for line in requests:               
        parts = line.split()           
        d = {                         
            "IP": parts[0],
            "METHOD": parts[1],
            "PATH": parts[2],
            "STATUS": parts[3],
        }
        result.append(d)          
    return result

print(line_dic(requests))
