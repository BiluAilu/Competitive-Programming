class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        targets = []
        for num in range(len(nums) - 1, 0, -1):
            for index in range(num):
                if nums[index] > nums[index + 1]:
                    nums[index], nums[index + 1] = nums[index + 1], nums[index]
        for num in range(len(nums)):
            if nums[num] == target:
                targets.append(num)
        return targets