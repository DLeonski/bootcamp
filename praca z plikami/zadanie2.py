import sys

login = {}
end = {}
with open(sys.argv[1]) as f:

    for i in f:
        i = i.split(";")
        user = i[0]
        action = i[1]
        time = i[2]
        time = int(time)

        if action == "LOGIN":
            login[user] = time
        if action == "LOGOUT":
            end[user] = end.get(user, 0) + time - login[user]



def sort(x):
    return x[1]

print("Czas przebywania: ")
for s in sorted(login.items() ,key=lambda x: x[1], reverse=True):
 print (s)