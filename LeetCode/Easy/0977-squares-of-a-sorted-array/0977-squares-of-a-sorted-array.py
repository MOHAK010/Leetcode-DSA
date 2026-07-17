class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        ans = [0] * len(nums)
        k = len(nums) - 1

        while left <= right :
            if abs(nums[left]) > abs(nums[right]):
                ans[k] = nums[left]**2
                left += 1
            else:
                ans[k] = nums[right]**2
                right -= 1

            k -= 1
        return ans
