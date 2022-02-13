infile = open('AI.txt', 'r')

sentence = infile.readline()
tempList = sentence.split()
sentenceList = []
for word in tempList:
    temp = ''
    if not word.isalnum():
        for char in word:
            if char.isalnum():
                temp+=char              
        word=temp
    sentenceList.append(word)
print(sentenceList)

wordCount = {}

for x in sentenceList:
    value = sentenceList.count(x)
    print(x, value)
    value = wordCount[x]
