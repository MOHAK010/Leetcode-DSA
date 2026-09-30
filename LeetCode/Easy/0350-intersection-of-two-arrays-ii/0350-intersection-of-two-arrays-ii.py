class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        result = []
        freq= {}
        for i in range(len(nums1)):
            if nums1[i] in freq:
                freq[nums1[i]] += 1
            else:
                freq[nums1[i]] = 1

        for i in range(len(nums2)):
            if nums2[i] in freq and freq[nums2[i]] > 0:
                result.append(nums2[i])
                freq[nums2[i]] -= 1
        return result 