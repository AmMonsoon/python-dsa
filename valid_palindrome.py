"""
# Problem

Valid Palindrome

## Pattern

Two Pointers

Use two pointers when you need to compare or process elements from both ends of a sequence efficiently.

## Optimized Solution

### Solution 1 (Clean String)

- Remove all non-alphanumeric characters.
- Convert the string to lowercase.
- Initialize two pointers:
  - `left = 0`
  - `right = len(string) - 1`
- While `left < right`:
  - Compare the characters.
  - If they don't match, return `False`.
  - Otherwise, increment `left` and decrement `right`.
- If the loop finishes, return `True`.

### Interview Optimization (O(1) Extra Space)

- Do **not** create a new string.
- Use two pointers on the original string.
- Move `left` forward until it points to an alphanumeric character.
- Move `right` backward until it points to an alphanumeric character.
- Compare the lowercase versions of both characters.
- Return `False` immediately on a mismatch.
- Continue until the pointers cross.

## Time Complexity

**O(n)**

Reason:
- Each character is visited at most once by the two pointers.
- Even when skipping punctuation, each pointer only moves forward (or backward) through the string.

## Space Complexity

### Clean String Solution

**O(n)**

Reason:
- A new normalized string is created.

### Interview Optimized Solution

**O(1)**

Reason:
- No additional string or data structure is created.
- Only a few variables (`left`, `right`) are used.
"""

"""python
while left < right:


not a `for` loop.
"""

def isPalindrome(s):
    stringList = s.replace(",", "").replace(":", "").replace(" ", "")
    lowerString = stringList.lower()
    left = 0
    right = len(lowerString) - 1

    for letter in lowerString:
        if lowerString[left] != lowerString[right]:
            return False
        left += 1
        right -= 1 
    return True






print(isPalindrome("A man, a plan, a canal: Panama")) #true
print(isPalindrome("race a car")) #false
print(isPalindrome(" ")) #true