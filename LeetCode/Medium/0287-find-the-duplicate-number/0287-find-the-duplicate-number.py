class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        frequency = {}

        for num in nums:
            if num in frequency:
                return num
            else:
                frequency[num] = 1