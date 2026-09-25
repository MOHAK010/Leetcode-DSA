class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr):

        # Merge Sort
        def merge_sort(arr):

            if len(arr) <= 1:
                return arr

            mid = len(arr) // 2

            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])

            result = []
            i = 0
            j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            while i < len(left):
                result.append(left[i])
                i += 1

            while j < len(right):
                result.append(right[j])
                j += 1

            return result

        arr = merge_sort(arr)

        # First element must be 1
        arr[0] = 1

        # Adjacent difference maximum 1
        for i in range(len(arr) - 1):
            if arr[i + 1] > arr[i] + 1:
                arr[i + 1] = arr[i] + 1

        return arr[-1]