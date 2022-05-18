from asyncore import file_dispatcher
import filecmp
import pickle

def dictionarySave(dictName, filePath):
    '''
    This function is used to save a dictionary to file
    '''
    with open(filePath, 'wb') as file:
        pickle.dump(dictName, file)


def dictionaryRead(filePath):
    '''
    This function is used to read a file given a file path
    '''
    with open(filePath, 'rb') as file:
        return pickle.load(file)