"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

def topKFrequent(nums, k):
    count = {}
    result = []
    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    buckets = [ [] for _ in range(len(nums) + 1) ]
    
    for num, frequency in count.items():
        buckets[frequency].append(num)
    
    for i in range(len(buckets) - 1, 0, -1):
       for num in buckets[i]:
        result.append(num)
        
        if len(result) == k:
            return result


print(topKFrequent([1,1,1,2,2,3], 2)) # [1,2]
print(topKFrequent([1], 1)) #[1]
print(topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)) #[1,2]

"""
First Solution not using bucket sort
Time Complexity: O(n log n)
Space Complexity: O(u)
  
    count = {}

    for num in nums:
        if num in count:
            count[num] += 1
        else:
            count[num] = 1
    
    pairs = list(count.items())
    sorted_pairs = sorted(pairs, key=lambda pair: pair[1], reverse=True)
    return [pair[0] for pair in sorted_pairs[:k]]
"""
    