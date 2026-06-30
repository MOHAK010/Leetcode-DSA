class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        arr = []
        for i in range(len(nums) - k, len(nums)):
            arr.append(nums[i])
        for i in range(0, len(nums) - k):
            arr.append(nums[i])
        for i in range(len(nums)):
            nums[i] = arr[i]