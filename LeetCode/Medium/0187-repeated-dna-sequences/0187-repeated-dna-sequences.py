class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        left = 0
        seen = set()
        repeated = set()

        for right in range(len(s)):

            if (right - left + 1) > 10:
                left += 1

            if (right - left + 1) == 10:

                dna = s[left:right+1]

                if dna in seen:
                    repeated.add(dna)
                else:
                    seen.add(dna)

        return list(repeated)