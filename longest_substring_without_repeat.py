"""
Given a string s, find the length of the longest substring without duplicate characters.
Time Complexity: O(n)
Space Complexity: O(n)
"""

def lengthOfLongestSubstring(s):
    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        seen.add(s[right])
        current_length = (right - left) + 1
        if(current_length > max_length):
            max_length =  current_length
    return max_length
    



print(lengthOfLongestSubstring("abcabcbb")) # 3
print(lengthOfLongestSubstring("bbbbb")) # 1
print(lengthOfLongestSubstring("pwwkew")) # 3