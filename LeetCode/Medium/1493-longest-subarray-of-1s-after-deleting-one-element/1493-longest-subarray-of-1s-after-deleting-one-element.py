class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_len = 0
        zero_count = 0
        left = 0

        # Right pointer ko ek-ek karke aage badhao
        for right in range(len(nums)):

            # Agar naya element 0 hai to zero_count badhao
            if nums[right] == 0:
                zero_count += 1

            # Agar 1 se zyada zero ho gaye
            # to window chhoti karo
            while zero_count > 1:

                # Agar bahar jane wala element 0 hai
                # to zero_count kam karo
                if nums[left] == 0:
                    zero_count -= 1

                # Left ko aage badhao
                left += 1

            # Ek element delete karna compulsory hai
            # Isliye window length = right - left
            max_len = max(max_len, right - left)

        return max_len