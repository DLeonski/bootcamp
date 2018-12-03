x = 0
with open("info.txt", "w", encoding='utf-8') as f:
    for i in range(10):
        x += 1
        f.write(str(x) + " ")
        f.write("Jakiś test\n")

# # tryb do odczytu
# with open ("info.txt",'w', encoding = 'utf-8') as f:
#     for i in range(10):
#         f.write("Jakiś tekst\n")
#
#
# with open ("info.txt", 'a', encoding = 'utf-8') as f:
#         f.write("Inny tekst")
