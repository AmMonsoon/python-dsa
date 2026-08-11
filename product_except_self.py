def productExceptSelf(nums):
    left = [1]
    right = [1]
    answer = []

    for i in range(1, len(nums)):
        left.append(left[i - 1] * nums[i - 1])
    
    for i in range(len(nums) - 2, -1, -1):
        right.append(right[-1] * nums[i + 1])
    right.reverse()

    for i in range(len(nums)):
        result = left[i] * right[i]
        answer.append(result)
    return answer

        
    
print(productExceptSelf([1,2,3,4])) # [24,12,8,6]
print(productExceptSelf([-1,1,0,-3,3])) # [0,0,9,0,0]

