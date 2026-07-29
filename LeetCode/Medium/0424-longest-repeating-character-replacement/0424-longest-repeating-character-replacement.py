class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        left = 0
        max_len = 0
        max_freq = 0
        freq_count = {}

        for right in range(len(s)):

            # Right character ko window me add karo
            if s[right] not in freq_count:
                freq_count[s[right]] = 1
            else:
                freq_count[s[right]] += 1

            # Current window ki maximum frequency update karo
            max_freq = max(max_freq, freq_count[s[right]])

            # Agar replace karne wale characters k se zyada ho gaye
            while (right - left + 1) - max_freq > k:

                # Left character ko window se hatao
                freq_count[s[left]] -= 1

                # Frequency 0 ho gayi to dictionary se delete kar do
                if freq_count[s[left]] == 0:
                    del freq_count[s[left]]

                # Left pointer aage badhao
                left += 1

            # Maximum valid window update karo
            max_len = max(max_len, right - left + 1)

        return max_len
