subtitles = {}
readfile = open("./task1.txt")
key = readfile.readline().replace("\n", "")
while key:
    subtitles[key] = readfile.readline().replace("\n", "")
    key = readfile.readline().replace("\n", "")
readfile.close()
# writefile = open("./task1_subtitles.txt", "wt")
# for text in subtitles.values():
#     writefile.write(text)
# writefile.close()

readfile = open("./task1.txt")
writefile = open("./task1_subtitles.txt", "wt")
for line in readfile.readlines()[1::2]:
    writefile.write(line.replace("\n", ""))
readfile.close()
writefile.close()
