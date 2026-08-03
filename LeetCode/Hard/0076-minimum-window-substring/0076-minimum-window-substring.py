class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        required_freq = {}
        window_freq = {}

        for ch in t:
            if ch not in required_freq:
                required_freq[ch] = 1
            else:
                required_freq[ch] += 1

        left = 0

        total_required_chars = len(required_freq)
        completed_chars = 0

        smallest_window = float("inf")
        answer_start = 0

        for right in range(len(s)):

            if s[right] not in window_freq:
                window_freq[s[right]] = 1
            else:
                window_freq[s[right]] += 1

            if (
                s[right] in required_freq
                and window_freq[s[right]] == required_freq[s[right]]
            ):
                completed_chars += 1

            while completed_chars == total_required_chars:

                if (right - left + 1) < smallest_window:
                    smallest_window = right - left + 1
                    answer_start = left

                window_freq[s[left]] -= 1

                if (
                    s[left] in required_freq
                    and window_freq[s[left]] < required_freq[s[left]]
                ):
                    completed_chars -= 1

                left += 1

        if smallest_window == float("inf"):
            return ""

        return s[answer_start : answer_start + smallest_window]
