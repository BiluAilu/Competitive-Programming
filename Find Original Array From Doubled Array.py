from collections import Counter


class Solution:
    def findOriginalArray(self, nums):
        nums.sort()
        counts = Counter(nums)
        temp = []
        for num in nums:
            if counts[num] > 0:
                counts[num] -= 1
            else:
                continue
                
            double = num * 2
            if double in counts and counts[double] > 0:
                temp.append(num)
                counts[double] -=1
            
        if len(temp) == len(nums)/2:
            return temp
        return []
        