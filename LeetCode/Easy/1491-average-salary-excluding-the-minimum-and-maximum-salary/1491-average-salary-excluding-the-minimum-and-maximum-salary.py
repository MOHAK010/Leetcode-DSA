class Solution:
    def average(self, salary: list[int]) -> float:
        largest = salary[0]
        smallest = salary[0]

        for num in salary:
            if num > largest :
                largest = num 
            
            if num < smallest:
                smallest = num 

        sum = 0
        count = 0 

        for num in salary :
            if num == largest or num == smallest:
                continue

            sum = sum + num
            count += 1

            average = sum / count 
        return average