class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        freq_count = {}
        max_len = 0

        for right in range(len(s)):

            if s[right] not in freq_count:
                freq_count[s[right]] = 1
            else:
                freq_count[s[right]] += 1

            while freq_count[s[right]] > 1:

                freq_count[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len