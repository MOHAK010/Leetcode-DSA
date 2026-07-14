class Solution:
    def firstUniqChar(self, s: str) -> int:

        freq = {}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] = freq[s[i]] + 1
            else:
                freq[s[i]] = 1

        for j in range(len(s)):
            if freq[s[j]] == 1:
                return j

        return -1