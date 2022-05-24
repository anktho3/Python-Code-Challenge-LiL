from distutils.dep_util import newer
from importlib.machinery import WindowsRegistryFinder
import string

def count_words(documentName):
    totalWordcount = 0
    wordCount = {}
    docFile = open(documentName)
    readableDoc = docFile.read()
    newRead = readableDoc.strip(".,[]_*")
    for word in readableDoc.strip(".,[]_*").split():
        if word in string.ascii_letters:
            totalWordcount += 1
            try:
                newVal = wordCount.get(word) + 1
                wordCount.update({word.strip(".,[]_*").upper():int(newVal)})
            except:
                wordCount.update({word.strip(".,[]_*").upper():1})
        elif word in string.punctuation:
            break
        elif word in string.digits:
            break
        else:
            totalWordcount += 1
            try:
                newVal = wordCount.get(word) + 1
                wordCount.update({word.strip(".,[]_*").upper():int(newVal)})
            except:
                wordCount.update({word.strip(".,[]_*").upper():1})

    print("Total Words:", totalWordcount)
    print("Top 20 Words: ")
    y = 0
    for x in sorted(wordCount, key=wordCount.get, reverse=True):
        print(x, wordCount[x])
        y += 1
        if y == 20:
            break
        else:
            continue
    return newRead
    # print(wordCount)
    # for i in sorted (wordCount.values()):
    #     for z in range(20):
    #         print(i,wordCount[i])
    #     break


    
    