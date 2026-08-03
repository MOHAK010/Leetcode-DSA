class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 
        freq_s1 = {}
        freq_window = {}

        for ch in s1:
            if ch not in freq_s1:
                freq_s1[ch] = 1
            else:
                freq_s1[ch] += 1
        left = 0

        for right in range(len(s2)):
            if s2[right] not in freq_window:
                freq_window[s2[right]]  = 1
            else:
                freq_window[s2[right]]  += 1

            if (right - left + 1) > len(s1):
                freq_window[s2[left]] -= 1
            
                if freq_window[s2[left]] == 0:
                    del freq_window[s2[left]]

                left += 1
            
            if freq_window == freq_s1:
                return True
                
        return False
