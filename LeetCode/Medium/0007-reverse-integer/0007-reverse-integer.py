class Solution:
    def reverse(self, x: int) -> int:
        negative = False 

        while x < 0:
            negative = True
            x = -x
        
        reverse = 0

        while x > 0:
            digit = x % 10
            reverse = reverse * 10 + digit
            x = x // 10

        if negative :
                reverse = -reverse

        if reverse < -2147483648 or reverse > 2147483647:
                return 0
                
        return reverse