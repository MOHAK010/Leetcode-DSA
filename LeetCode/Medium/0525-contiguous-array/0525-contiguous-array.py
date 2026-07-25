class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_index = {0: -1}
        prefix_sum = 0
        ans = 0

        for i in range(len(nums)):

            if nums[i] == 0:
                prefix_sum -= 1
            else:
                prefix_sum += 1

            if prefix_sum in prefix_index:
                ans = max(ans, i - prefix_index[prefix_sum])
            else:
                prefix_index[prefix_sum] = i

        return ans