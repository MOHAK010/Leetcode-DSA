class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hashmap = {}          # Jo numbers dekh liye unko yaad rakhne ka bag

        for i in range(len(numbers)):      # Ek-ek number uthao

            need = target - numbers[i]     # Is number ke saath target banane ke liye aur kya chahiye?

            if need in hashmap:         # Agar wo pehle mil gaya
                return (hashmap[need]+1, i+1)   # To answer mil gaya

            hashmap[numbers[i]] = i        # Warna is number ko yaad rakh lo

        return -1