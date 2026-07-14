class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}

        for i in range(len(s)):
            if s[i] in freq:
                freq[s[i]] = freq[s[i]] + 1
            else:
                freq[s[i]] = 1

        for j in range(len(t)):
            if t[j] not in freq:
                return False

            freq[t[j]] = freq[t[j]] - 1

            if freq[t[j]] < 0:
                return False

        for value in freq.values():
            if value != 0:
                return False

        return True