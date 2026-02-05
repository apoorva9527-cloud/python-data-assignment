def calculate_average(scores):
    return sum(scores) / len(scores)

def has_admin_access(roles):
    return "admin" in roles

def main():
    user = {
        "name": "Alice",
        "scores": [80, 85],   # 👈 EXACT 82.5
        "roles": {"admin", "editor"}
    }

    print("Name:", user["name"])
    print("Average Score:", calculate_average(user["scores"]))
    print("Admin Access:", has_admin_access(user["roles"]))

main()
