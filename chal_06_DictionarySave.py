import json
import random

def dictionarySave(dictName, filePath):
    file = open(f"{filePath}/file{random.randint(0,50)}", "x")
    file.write(str(dictName))
    file.close()
    print(file.name)


def dictionaryRead(fileName):
    '''
    This function is used to read a file given a file path
    '''
    file = open(fileName, "r")
    print(file.read())
    return file.read()