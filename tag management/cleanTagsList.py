import re

rawTagsFile = open("rawTags.txt", "r")
cleanTagsFile = open("tags.csv", "w")

while True:
    line = rawTagsFile.readline()
    if line:
        # erase number at the end
        tag = re.search("([^\()]*)", line).group(1)
        cleanTagsFile.write(tag.strip() + ",")
    else: 
        break