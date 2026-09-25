class Solution:
    def countDigits(self, n: int) -> int:
        if n < 10:
           return 1

        num = n
        count = 0

        while num > 0:
            digit = num % 10

            if digit != 0:
                if n % digit == 0:
                    count += 1

            num = num // 10

        return count