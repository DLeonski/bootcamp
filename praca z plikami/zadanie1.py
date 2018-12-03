import sys
print(sys.argv)

with open(sys.argv[1]) as f:
    x = 0
    for i in f:
        x += 1
        print(x, i, end = "")


try:
    print(sys.argv)
except IndexError:
    print("Zapomniałeś podac nazwe pliku")


# x = 0
# with open("info.txt", "w", encoding='utf-8') as f:
#     for i in range(10):
#         x += 1
#         f.write(str(x) + " ")
#         f.write("Jakiś test\n")
#