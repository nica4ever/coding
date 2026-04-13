# 18. Same format. Return a dict {username: list of actions they did}.

from collections import defaultdict

logs = [
    "2024-03-15 10:00:01 user=alice action=login",
    "2024-03-15 10:00:05 user=bob action=upload_file",
    "2024-03-15 10:00:08 user=alice action=view_dashboard",
    "2024-03-15 10:00:12 user=carol action=login",
    "2024-03-15 10:00:18 user=alice action=download",
    "2024-03-15 10:00:22 user=dave action=login",
    "2024-03-15 10:00:30 user=bob action=logout",
    "2024-03-15 10:00:35 user=alice action=upload_file",
    "2024-03-15 10:00:40 user=carol action=download",
    "2024-03-15 10:00:45 user=eve action=login",
    "2024-03-15 10:00:50 user=alice action=logout",
    "2024-03-15 10:00:55 user=bob action=view_dashboard",
]

def actions(logs):
    user_actions = defaultdict(list)
    for line in logs:
        user = line.split()[2].split("=")[1]
        action = line.split()[3].split("=")[1]
        user_actions[user].append(action)
    return dict(user_actions)
print(actions(logs))
