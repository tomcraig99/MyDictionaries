#open file
infile = open('AI.txt', 'r')
#get rid of special characters
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
#create dictionary
wordCount = {}
#add keys to dictionary
for key in sentenceList:
    value = sentenceList.count(key)
    wordCount[key.lower()] = value
#display keys and their values
for key in wordCount:
    print(key, wordCount[key])