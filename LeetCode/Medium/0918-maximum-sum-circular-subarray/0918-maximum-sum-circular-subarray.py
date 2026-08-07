class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sum = nums[0]
        min_sum = nums[0]

        current_max = nums[0]
        current_min = nums[0]

        total_sum = sum(nums)

        for i in range(1,len(nums)):

            current_max = max(nums[i] , current_max + nums[i])
            max_sum =  max(current_max , max_sum)
            current_min = min(nums[i] , current_min + nums[i])
            min_sum = min(current_min , min_sum)
            
        if max_sum < 0 :
            return max_sum 

        return max(max_sum,total_sum - min_sum)