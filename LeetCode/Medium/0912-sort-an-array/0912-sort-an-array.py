class Solution:
    def sortArray(self, nums):
        def merge_sort(nums):

            # 1. Agar 1 ya 0 element hai → already sorted
            if len(nums) <= 1:
                return nums

            # 2. Array ko divide karo
            mid = len(nums) // 2

            left = nums[:mid]
            right = nums[mid:]

            # 3. Left aur Right ko recursively divide karo
            left = merge_sort(left)
            right = merge_sort(right)

            # 4. Dono sorted parts ko merge karo
            new = []

            i = 0
            j = 0

            # 5. Dono parts ke elements compare karo
            while i < len(left) and j < len(right):

                if left[i] <= right[j]:
                    new.append(left[i])
                    i += 1
                else:
                    new.append(right[j])
                    j += 1

            # 6. Left mein kuch bach gaya
            while i < len(left):
                new.append(left[i])
                i += 1

            # 7. Right mein kuch bach gaya
            while j < len(right):
                new.append(right[j])
                j += 1

            return new

        return merge_sort(nums)
        