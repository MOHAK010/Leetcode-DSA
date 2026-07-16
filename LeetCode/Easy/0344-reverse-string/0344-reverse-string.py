class Solution:
    def reverseString(self, s: List[str]) -> None:
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]   # Swap

            left += 1
            right -= 1
        return 
        """
        Do not return anything, modify s in-place instead.
        """
       