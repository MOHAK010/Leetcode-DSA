class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        if len(p) > len(s):
            return []

        freq_p = {}
        freq_window = {}
        left = 0
        ans = []

        # p ki frequency
        for ch in p:
            if ch not in freq_p:
                freq_p[ch] = 1
            else:
                freq_p[ch] += 1

        for right in range(len(s)):

            # Right add
            if s[right] not in freq_window:
                freq_window[s[right]] = 1
            else:
                freq_window[s[right]] += 1

            # Window ko fixed size me rakho
            if (right - left + 1) > len(p):

                freq_window[s[left]] -= 1

                if freq_window[s[left]] == 0:
                    del freq_window[s[left]]

                left += 1

            # Match mila
            if freq_window == freq_p:
                ans.append(left)     # ⭐ Starting index store

        return ans