def merge(nums1, m, nums2, n):
    i = m - 1
    j = n - 1
    k = (m + n) - 1

    while j >= 0:
        
        if nums2[j] >= nums1[i]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        if i < 0:
            return nums1
        k -= 1


    return nums1

# print(merge([1,2,3,0,0,0], 3, [2,5,6], 3))  #[1,2,2,3,5,6]
# print(merge([0], 0, [1], 1))
print(merge([2, 0], 1, [1], 1)) #[1, 2]