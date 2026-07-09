class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        a = 0  # left index
        b = 0  # zero count
        c = 0  # maximum length

        for i in range(len(nums)):

            if nums[i] == 0:
                b += 1

            while b > k:
                if nums[a] == 0:
                    b -= 1
                a += 1

            c = max(c, i - a + 1)

        return c