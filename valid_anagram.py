# Problem

Valid Anagram

## Pattern

Hash Map

Use a hash map when you need to compare how many times each value appears.

## Optimized Solution

- Return `False` immediately if the strings have different lengths.
- Count the frequency of each character in the first string.
- Iterate through the second string:
  - If the character is missing, return `False`.
  - Decrement its count.
  - If the count becomes negative, return `False`.
- If the loop finishes, return `True`.

## Time Complexity

**O(n)**

Reason:
- One pass to build the frequency map.
- One pass to consume it.
- Sequential loops: `O(n) + O(n) = O(n)`.

## Space Complexity

**O(n)**

Reason:
- The frequency map may store up to all unique characters in the input.

def isAnagram(s, t):
    if len(s) != len(t): return False

    letterCount = {}

    for letter in s:
        if letter in letterCount:
            letterCount[letter] += 1
        else:
            letterCount[letter] = 1

    for letter in t:
        if letter not in letterCount:
            return False
        else:
            letterCount[letter] -= 1
            if letterCount[letter] < 0: return False
    
    return True


print(isAnagram("anagram", "nagaram")) #true
print(isAnagram("rat", "car")) #false
