class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        a = 0
        for i in range(len(nums)):
            if nums[a] == nums[i]:
                continue
            else:
                a += 1
                nums[a] = nums[i]
        return a+1
              