class Solution:
    def reverseWords(self, s: str) -> str:
        result = ""
        word = []

        for i in range(len(s)):

            if s[i] != " ":
                word.append(s[i])

            else:
                i = 0
                j = len(word) - 1

                while i < j:
                    word[i], word[j] = word[j], word[i]
                    i += 1
                    j -= 1

                for k in range(len(word)):
                    result += word[k]

                result += " "
                word = []

        i = 0
        j = len(word) - 1

        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1

        for k in range(len(word)):
            result += word[k]

        return result