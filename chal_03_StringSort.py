def stringSort(inputString):
    loadedString = [word for word in inputString.split()]
    sortedString = loadedString
    sortedString.sort(key=str.lower)
    return sortedString
