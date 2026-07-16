def find_capitals(word):
    indexes = []
    for index, letter in enumerate(word):
        if letter == letter.upper():
            indexes.append(index)
    return indexes



print(find_capitals('CodEWaRs')) # [0,3,4,6] 