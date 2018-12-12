import re
regex = re.compile("\d{2}-\d{3}")

kody = regex.findall("21-370dsadas44-500dsadadjp2-gmda")
print(kody)

regex_data = re.compile("\d{2} \d{2} \d{4}")
regex_mail = re.compile("([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\..{2,3})")

# ^[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$

maile = regex_mail.findall("asdasd@adsaa.pldjfej555@5555@dsada.pl")
print(maile)