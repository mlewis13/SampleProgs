#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
storyFile = open('story.txt', 'r')

temp = []
wordsInStory = []

for line in storyFile:
    temp.append(line.split())

for line in temp:
    for item in line:
        if ((item.isalpha()) and item.islower()):
            wordsInStory.append(item)


#wordsInStory = list(tempset)
#wordsInStory.sort()

print(wordsInStory)
