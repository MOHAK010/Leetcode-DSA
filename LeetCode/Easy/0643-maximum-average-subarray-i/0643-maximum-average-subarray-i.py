class Solution:
    def findMaxAverage(self, nums, k):

        a = sum(nums[:k])
        b = a

        for i in range(k, len(nums)):
            a = a - nums[i-k] + nums[i]
            b = max(a, b)

        return b / k