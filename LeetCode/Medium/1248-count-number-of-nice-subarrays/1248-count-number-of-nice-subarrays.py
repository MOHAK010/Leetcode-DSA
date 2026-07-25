class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        total_kutte = 0
        dekhe_kutte = {0:1}
        ans = 0

        for i in range(len(nums)):

            if nums[i] % 2 == 1:
                total_kutte += 1

            chahiye_kutte = total_kutte - k

            if chahiye_kutte in dekhe_kutte:
                ans += dekhe_kutte[chahiye_kutte]

            if total_kutte in dekhe_kutte:
                dekhe_kutte[total_kutte] += 1
            else:
                dekhe_kutte[total_kutte] = 1
        return ans