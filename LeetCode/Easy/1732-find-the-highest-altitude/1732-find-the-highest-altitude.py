class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        current = 0
        highest = 0

        for i in range(len(gain)):
            current += gain[i]
            highest = max(highest, current)

        return highest