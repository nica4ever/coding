# 5.18 Using the list from 5.17, write a loop that prints only requests
#      with status "404".
requests = [
    "10.0.0.1 GET /index.html 200",
    "10.0.0.2 POST /api/login 404",
    "10.0.0.1 GET /style.css 200",
    "10.0.0.3 GET /admin 404",
    "10.0.0.2 POST /api/login 404",
]

def get_request(request):
    result = []
    for line in request:
            parts = line.split()
            if parts[3] == "404":
                dic = {
                        "IP": parts[0],
                        "METHOD": parts[1],
                        "PATH": parts[2],
                        "STATUS": parts[3],
                    }
                result.append(dic)
    return result
print(get_request(requests))


