class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        minmaxpairsum = 0
        nums.sort()
        for i in range(len(nums) // 2):
            minmaxpairsum = max(nums[i] + nums[-(i + 1)], minmaxpairsum)
        return minmaxpairsum