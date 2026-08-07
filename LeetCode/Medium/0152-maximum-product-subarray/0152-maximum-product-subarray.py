class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        answer = nums[0]


        for i in range(1,len(nums)):

            temp = current_max

            current_max = max(nums[i], current_max * nums[i] , current_min * nums[i])
            current_min = min( nums[i] , temp * nums[i] , current_min * nums[i])

            answer = max(answer , current_max)

        return answer