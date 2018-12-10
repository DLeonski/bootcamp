import sys

user_last_login = {}
user_total_time = {}
with open(sys.argv[1]) as f:
    for line in f:
        user, action, time_str = line.split(";")
        time = int(time_str)
        user = line[0]
        action = line[1]
        time = line[2]

        if action == "LOGIN":
            user_last_login[user] = time
        elif action == "LOGOUT":
            time_temp = time - user_last_login[user]
            user_total_time[user] = user_total_time.get(user, 0) + time_temp

for user, time in user_total_time.items():
    print(f"- {user}: {time} s")


def nazwa(x):
    return x[1]


# #
print("Czas przebywania: ")
for user, time in sorted(user_total_time.items()):
    print(f"{user}: {time} s")

