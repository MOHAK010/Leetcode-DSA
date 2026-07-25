class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        answer = 0
        count = {0:1}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            reminder = sum % k
            if reminder in count:
                answer += count[reminder]
                count[reminder] += 1
            else:
                count[reminder] = 1
        return answer  