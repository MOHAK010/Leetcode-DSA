class Solution:
    def missingNumber(self, nums: list[int]) -> int:

        freq = {}

        for num in nums:
            freq[num] = 1
        for num in range(len(nums)+ 1):
            if num not in freq:
                return num
