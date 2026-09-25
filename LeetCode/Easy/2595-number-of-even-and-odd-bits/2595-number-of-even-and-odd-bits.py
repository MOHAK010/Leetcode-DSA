class Solution:
    def evenOddBit(self, n: int) -> list[int]:
        odd = 0
        even = 0
        i = 0
        while n > 0:
            bit = n % 2 

            if bit == 1:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1

            n = n // 2
            i += 1
        return [even,odd]