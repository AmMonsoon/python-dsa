"""
Time: O(n)
Space: O(n)
"""

def isValid(s):
    stack = []
    pairs = {
        ")" : "(",
        "]" : "[",
        "}" : "{"
    }

    for el in s:
        if el in pairs:
            if not stack:
                return False
            if stack[-1] != pairs[el]:
                return False
            stack.pop()
        else:
            stack.append(el)

    return len(stack) == 0
        
print(isValid("()")) # True
print(isValid("()[]{}")) # True
print(isValid("(]")) # False
print(isValid("([])")) # True
print(isValid("([)]")) # False