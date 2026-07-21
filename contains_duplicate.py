# Problem

Contains Duplicate

## Pattern

Hash Set / Hash Map

Use a Hash Set when you only need to know whether you've seen a value before.

Use a Hash Map when you need additional information such as a count or an index.

## Optimized Solution

- Create an empty set.
- Iterate through the array once.
- For each number:
  1. Check whether it already exists in the set.
  2. If it does, return `True`.
  3. Otherwise, add it to the set.
- If the loop finishes, return `False`.

```python
def containsDuplicate(nums):
    seen = set()

    for num in nums:
        if num in seen:
            return True

        seen.add(num)

    return False
```

## Time Complexity

Dictionary (improved): **O(n)**

Set: **O(n)**

Reason:
- Iterate through the list once.
- Set lookups and insertions are O(1) on average.

## Space Complexity

Dictionary: O(n)

Set: O(n)

Reason:
- In the worst case, every element is unique and stored in the hash table.

def containsDuplicate(nums):
    numberList = {}
    count = 0
    for num in nums:
        if num in numberList:
            return True
        else:
            numberList[num] = count
            
    return False






print(containsDuplicate([1,2,3,1])) #true