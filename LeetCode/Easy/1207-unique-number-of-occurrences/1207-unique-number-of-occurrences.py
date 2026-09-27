class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        frequency = {}
        for num in arr:

            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        for num1 in frequency :
            for num2 in frequency :
                if num1 != num2:
                   if frequency[num1] == frequency[num2]:

                        return False 
        return  True
    