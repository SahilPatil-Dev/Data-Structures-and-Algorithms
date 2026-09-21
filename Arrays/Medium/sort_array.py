class Solution:

    # Brute Force - Merge Sort
    def sortArray_merge_sort(arr: list):
        """
        Sort the array using merge sort.
        Time: O(n log n) | Space: O(n)
        """

        def merge(left, right):
            # Merging two sorted arrays → O(n)
            result = []
            i = j = 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    result.append(left[i])
                    i += 1
                else:
                    result.append(right[j])
                    j += 1

            # Append remaining elements
            result.extend(left[i:])
            result.extend(right[j:])

            return result

        def merge_sort(nums):
            # Splitting recursively → O(log n) levels
            if len(nums) <= 1:
                return nums

            mid = len(nums) // 2

            left = merge_sort(nums[:mid])
            right = merge_sort(nums[mid:])

            return merge(left, right)

        sorted_arr = merge_sort(arr)

        # Copy sorted result back → O(n)
        for i in range(len(arr)):
            arr[i] = sorted_arr[i]


    # Better - Counting
    def sortArray_better(arr: list):
        """
        Count 0s, 1s and 2s, then overwrite the array.
        Time: O(n) | Space: O(1)
        """

        count0 = count1 = count2 = 0

        # One pass → O(n)
        for num in arr:
            if num == 0:
                count0 += 1
            elif num == 1:
                count1 += 1
            else:
                count2 += 1

        # Rewrite 0s → O(n) worst case
        for i in range(count0):
            arr[i] = 0

        # Rewrite 1s → O(n) worst case
        for i in range(count0, count0 + count1):
            arr[i] = 1

        # Rewrite 2s → O(n) worst case
        for i in range(count0 + count1, len(arr)):
            arr[i] = 2


    # Optimal - Dutch National Flag
    def sortArray_optimal(arr: list):
        """
        Sort 0s, 1s and 2s using three pointers.
        Time: O(n) | Space: O(1)
        """

        low = 0
        mid = 0
        high = len(arr) - 1

        # Intuition:
        # [0 ... low-1]       → all 0s
        # [low ... mid-1]     → all 1s
        # [mid ... high]      → unknown
        # [high+1 ... n-1]    → all 2s
        #
        # We process the unknown region until mid > high.

        while mid <= high:

            if arr[mid] == 0:
                # 0 belongs to the left section.
                # Swap it to the `low` boundary.
                arr[low], arr[mid] = arr[mid], arr[low]

                low += 1
                mid += 1

            elif arr[mid] == 1:
                # 1 is already in the correct middle section.
                mid += 1

            else:
                # 2 belongs to the right section.
                # Swap it with `high`.
                #
                # Do NOT increment mid here because the element
                # coming from `high` is still unprocessed.
                arr[mid], arr[high] = arr[high], arr[mid]

                high -= 1