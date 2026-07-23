class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        running_sum = 0
        min_sum = 0

        for i in range(len(nums)):
            running_sum = running_sum + nums[i]

            if running_sum < min_sum:
                min_sum = running_sum

        return abs(min_sum) + 1
