def twoSum(nums, target):
        pos = {}
        reverse ={}
        for i , n in enumerate(nums):
            pos[i] = n
            reverse[n] = i
        
        for p, v in pos.items():
            missing_num = target - v
            if missing_num in reverse:
                if reverse[missing_num] != p:
                    return [p, reverse[missing_num]]