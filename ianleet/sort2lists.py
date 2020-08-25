def merge(nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for t in range(n):
            nums1.pop(0)
        nums1 += nums2
        return nums1.sort()
    
merge([1,2,3,0,0,0], 3, [2,5,6], 3)