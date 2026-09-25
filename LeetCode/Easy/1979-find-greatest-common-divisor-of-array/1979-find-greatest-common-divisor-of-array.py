class Solution:
    def findGCD(self, nums):
        largest = nums[0]
        smallest = nums[0]

        for num in nums:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num

        while smallest != 0:
            remainder = largest % smallest
            largest = smallest
            smallest = remainder

        return largest