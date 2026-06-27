class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        diary = {}
        for i in range(len(nums)):
            if nums[i] in diary:
                diary[nums[i]] += 1
            else:
                diary[nums[i]] =1
        for key,value in diary.items():
           if value > len(nums) // 2:
            return key