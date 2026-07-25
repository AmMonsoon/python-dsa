"""
Time Complexity:O(n + m)
Space Complexity:O(n + m)

"""

def mergeAlternately(word1, word2):
    i = 0
    j = 0
    result = []
    
    while i < len(word1) and j < len(word2):    
        result.append(word1[i])
        result.append(word2[j])

        i += 1
        j += 1

    result.extend(word1[i:])
    result.extend(word2[j:])

    return "".join(result)


# print(mergeAlternately("abc", "pqr")) #"apbqcr"
print(mergeAlternately("ab", "pqrs")) #"apbqrs"
print(mergeAlternately("abcd", "pq")) #"apbqcd"