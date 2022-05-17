
# Default list
example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]


def index_all(listName, indexCrit):
    indices = list()
    for i in range(len(listName)):
        if listName[i] == indexCrit:
            indices.append([i])
        elif isinstance(listName[i],list):
            for index in index_all(listName[i], indexCrit):
                indices.append([i]+index)
    return indices

