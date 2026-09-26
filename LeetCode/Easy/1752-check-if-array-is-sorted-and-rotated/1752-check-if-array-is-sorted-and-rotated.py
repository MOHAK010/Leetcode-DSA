class Solution:
    def check(self, nums):
        break_count = 0
        n = len(nums)

        for i in range(n):
            if nums[i] > nums[(i + 1) % n]:
                break_count += 1

        if break_count > 1:
            return False

        return True