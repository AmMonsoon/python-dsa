def find_capitals(word):
    indexes = []
    letterList = list(word)
    for index, letter in enumerate(letterList):
        if letter == letter.upper():
            indexes.append(index)
    return indexes



print(find_capitals('CodEWaRs')) # [0,3,4,6] 