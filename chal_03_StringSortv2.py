def stringSort(inputString):
    return ' '.join(sorted(inputString.split(), key = str.casefold))
