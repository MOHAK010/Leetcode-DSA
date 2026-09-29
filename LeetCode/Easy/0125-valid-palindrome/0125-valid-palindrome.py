class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while j > i:
            if not s[i].isalnum():
                i+= 1
                continue
            if  not s[j].isalnum():
                j-=1
                continue
        
            if s[j].lower() == s[i].lower():
                j-= 1
                i+= 1
            else:
                return False
        return True 
