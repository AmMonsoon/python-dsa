# Find Capitals

## Pattern
String Traversal

## Optimized Solution
Iterate through each character in the string using `enumerate()` to keep track of
both the index and the character. If the character is uppercase, append its index
to the result list. Return the list after processing the entire string.

## Time Complexity
O(n)

## Space Complexity
O(k)

Where `k` is the number of capital letters in the string.
In the worst case (every character is uppercase), this becomes **O(n)**.

def find_capitals(word):
    indexes = []
    for index, letter in enumerate(word):
        if letter == letter.upper():
            indexes.append(index)
    return indexes



print(find_capitals('CodEWaRs')) # [0,3,4,6] 