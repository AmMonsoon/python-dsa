"""
Time Complexity: O(n log n)
Space Complexity: O(u)
"""

def topKFrequent(nums, k):
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    pairs = list(count.items())
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
    return [pair[0] for pair in sorted_pairs[:k]]
        


print(topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(topKFrequent([1], 1)) #[1]
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) #[1,2]