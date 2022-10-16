class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        continer = [-1] * len(nums1)
        for i in range(len(nums1)):
            find = False
            for j in range(len(nums2)):
                if nums2[j] == nums1[i]:
                    find = True
                elif find and nums2[j] > nums1[i]:
                    continer[i] = nums2[j]
                    break

        
        return continer