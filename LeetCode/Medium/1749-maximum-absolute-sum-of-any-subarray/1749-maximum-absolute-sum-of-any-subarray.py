class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        max_sum = nums[0]
        min_sum = nums[0]

        for i in range(1,len(nums)):
            current_max = max(current_max + nums[i] , nums[i])
            current_min = min(current_min + nums[i] , nums[i])

            max_sum = max(current_max , max_sum)
            min_sum = min(current_min , min_sum)
            
        return max(abs(max_sum), abs(min_sum))