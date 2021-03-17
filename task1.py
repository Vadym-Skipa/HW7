# Task 1
# У файлі task1.txt знаходиться текст субтитрів взятий з відео на ютубі. Текст складається з  міток часу і репліки яка була сказана в той момент часу.
# Причому репліка знаходиться в наступному рядку після мітки часу.
# Результатом виконнання завдання повинно бути:
# 1. словник елементами якого буде пара ключ:значення де ключ - мітка часу, значення - репліка в даний момент часу
# 2. файл в якому знаходиться текст з якого видалені всі мітки часу. всі субтитри повинні мати вигляд простого тексту.
# Це означає що окрім видалення міток часу, вам потрібно видалити переноси рядків

subtitles = {}
readfile = open("./task1.txt")
key = readfile.readline().replace("\n", "")
while key:
    subtitles[key] = readfile.readline().replace("\n", "")
    key = readfile.readline().replace("\n", "")
readfile.close()
# writefile = open("./task1_subtitles.txt", "wt")
# for text in subtitles.values():
#     writefile.write(text + " ")
# writefile.close()

readfile = open("./task1.txt")
writefile = open("./task1_subtitles.txt", "wt")
for line in readfile.readlines()[1::2]:
    writefile.write(line.replace("\n", " "))
readfile.close()
writefile.close()
