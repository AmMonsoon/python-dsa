"""
Time Complexity: O(n * k)
Space Complexity: O(n * k)

"""

def groupAnagrams(strs):
    words = {}
    key = ()
    
    for word in strs:
        count = [0] * 26

        for letter in word:
            index = ord(letter) - ord("a")
            count[index] += 1
        
       
        key = tuple(count)
        if key in words:
            words[key].append(word)
        else:
            words[key] = [word]
        
    return words.values()

        
    
        









print(groupAnagrams(["eat","tea","tan","ate","nat","bat"])) #[["bat"],["nat","tan"],["ate","eat","tea"]]
print(groupAnagrams([""])) # [[""]]
print(groupAnagrams(["a"])) # ["a"]]