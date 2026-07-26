"""
Time Complexity: O(n)
Space Complexity: O(1)

"""

def removeDuplicates(nums):
    write = 1
    read = 1

    while read < len(nums):
        if nums[write - 1] != nums[read]:
            nums[write] =  nums[read]
            write += 1
        read += 1
    return write


print(removeDuplicates([1,1,2])) # 2
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # 5