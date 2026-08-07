class Solution:
    def maximumSum(self, arr: List[int]) -> int:

        without_delete = arr[0]
        with_delete = arr[0]
        answer = arr[0]

        for i in range(1, len(arr)):

            temp = without_delete

            without_delete = max(arr[i], without_delete + arr[i])

            with_delete = max(temp, with_delete + arr[i])
            
            answer = max(answer, without_delete, with_delete)

        return answer