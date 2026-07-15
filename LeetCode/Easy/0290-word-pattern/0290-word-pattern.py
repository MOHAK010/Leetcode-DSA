class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
       
        str1 = {}
        str2 = {}

        words = s.split()

        if len(pattern) != len(words):
            return False

        for i in range(len(pattern)):

            if pattern[i] in str1:
                if str1[pattern[i]] != words[i]:
                    return False
            else:
                str1[pattern[i]] = words[i]

            if words[i] in str2:
                if str2[words[i]] != pattern[i]:
                    return False
            else:
                str2[words[i]] = pattern[i]

        return True