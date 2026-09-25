class Solution:
    def thirdMax(self, nums):
        largest = None
        second = None
        third = None

        for num in nums:

            if num == largest or num == second or num == third:
                continue

            if largest is None or num > largest:
                third = second
                second = largest
                largest = num

            elif second is None or num > second:
                third = second
                second = num

            elif third is None or num > third:
                third = num

        if third is None:
            return largest

        return third