class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        left = 0
        current_sum = 0
        max_sum = 0
        freq_count = {}

        for right in range(len(nums)):

            current_sum += nums[right]

            if nums[right] not in freq_count:
                freq_count[nums[right]] = 1
            else:
                freq_count[nums[right]] += 1

            while freq_count[nums[right]] > 1:

                freq_count[nums[left]] -= 1
                current_sum -= nums[left]

                if freq_count[nums[left]] == 0:
                    del freq_count[nums[left]]

                left += 1

            max_sum = max(max_sum, current_sum)

        return max_sum