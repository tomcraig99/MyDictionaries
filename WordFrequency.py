# open file
infile = open("AI.txt", "r")
# right sentence to list and split it up by spaces
sentence = infile.readline()
tempList = sentence.split()
sentenceList = []
# loop to write alphanumeric char to temp word and add to list
for word in tempList:
    temp = ""
    if not word.isalnum():
        for char in word:
            if char.isalnum():
                temp += char
        word = temp
    sentenceList.append(word.lower())
# create dictionary
wordCount = {}
# add keys to dictionary
for key in sentenceList:
    value = sentenceList.count(key)
    wordCount[key] = value
# display keys and their values
for key in wordCount:
    print(key, wordCount[key])
