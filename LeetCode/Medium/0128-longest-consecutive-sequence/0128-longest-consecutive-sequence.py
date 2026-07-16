class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
    

        num_set = set(nums)                  # Remove duplicates + O(1) lookup
        longest = 0

        for current in num_set:              # Sirf unique numbers

            if current - 1 not in num_set:   # Sequence ka start

                length = 1

                while current + 1 in num_set:

                    current += 1
                    length += 1

                longest = max(longest, length)

        return longest