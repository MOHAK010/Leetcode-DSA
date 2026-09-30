class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j] and nums1[i] not in result:
                    result.append(nums1[i])
        return result 