class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        left = 0
        freq_count = {}
        max_len = 0

        for right in range(len(fruits)):

            # Right wala fruit window me add karo
            if fruits[right] not in freq_count:
                freq_count[fruits[right]] = 1
            else:
                freq_count[fruits[right]] += 1

            # Agar 2 se zyada fruit types ho gaye
            while len(freq_count) > 2:

                # Left wale fruit ki frequency kam karo
                freq_count[fruits[left]] -= 1

                # Agar frequency 0 ho gayi to dictionary se delete kar do
                if freq_count[fruits[left]] == 0:
                    del freq_count[fruits[left]]

                # Left pointer aage badhao
                left += 1

            # Maximum window length update karo
            max_len = max(max_len, right - left + 1)

        return max_len