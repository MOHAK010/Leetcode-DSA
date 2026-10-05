class Solution:
    def maximumValueSum(self, nums, k, edges):
        total = 0
        count = 0
        min_gain = float('inf')

        for x in nums:
            xor_value = x ^ k

            if xor_value > x:
                total += xor_value
                count += 1
                min_gain = min(min_gain, xor_value - x)
            else:
                total += x
                min_gain = min(min_gain, x - xor_value)

        if count % 2 == 1:
            total -= min_gain

        return total