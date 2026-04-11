# 5.19 Using the list from 5.17, count how many requests each IP made.
#      Store in a dict {ip: count}. Print.

requests = [
    "10.0.0.1 GET /index.html 200",
    "10.0.0.2 POST /api/login 401",
    "10.0.0.1 GET /style.css 200",
    "10.0.0.3 GET /admin 403",
    "10.0.0.2 POST /api/login 401",
]

def count_requests(request):
    dic = {}
    for line in request:
        part = line.split()
        if part[0] in dic:
            dic[part[0]] += 1
        else:
            dic[part[0]] = 1
    return dic

print(count_requests(requests))

