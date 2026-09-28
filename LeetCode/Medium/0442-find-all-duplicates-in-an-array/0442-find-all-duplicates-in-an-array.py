class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:

        frequency = {}
        duplicates = []

        for num in nums:
            if num in frequency:
                duplicates.append(num)
            else:
                frequency[num] = 1

        return duplicates