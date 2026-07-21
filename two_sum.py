# Problem

Two Sum

## Pattern

Hash Map

## Time Complexity

Brute Force: **O(n²)**

Optimized: **O(n)**

Reason:
- Iterate through the array once.
- Dictionary lookups and insertions are **O(1)** on average.

## Space Complexity

Brute Force: **O(1)**

Optimized: **O(n)**

Reason:
- In the worst case, the dictionary stores every element before finding the answer.

#Brute Force solution
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]


def twoSum(nums, target):
    numLookUp = {}
    for index, num in enumerate(nums):
        neededNum = target - num
        if neededNum in numLookUp:
            return [numLookUp[neededNum], index]
        else:
            numLookUp[num] = index

        
       
print(twoSum([2,7,11,15], 9)) #[0,1]