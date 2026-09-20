class Solution:

    # Brute Force
    def TwoSum_brute_force(arr: list, target: int):
        """
        Check every possible pair.
        Time: O(n²) | Space: O(1)
        """
        n = len(arr)

        # Two nested loops → O(n²)
        for i in range(n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] == target:
                    return [i, j]

        return [-1, -1]


    # Better - Two Pointer
    def TwoSum_better(arr: list, target: int):
        """
        Sort and use two pointers.
        Time: O(n log n) | Space: O(n)
        """
        # Store value + original index → O(n) space
        nums = [(num, i) for i, num in enumerate(arr)]

        # Sorting → O(n log n)
        nums.sort()

        left = 0
        right = len(nums) - 1

        # One loop → O(n)
        while left < right:
            total = nums[left][0] + nums[right][0]

            if total == target:
                return [nums[left][1], nums[right][1]]

            elif total < target:
                left += 1

            else:
                right -= 1

        return [-1, -1]


    # Optimal - Hashing
    def TwoSum_optimal(arr: list, target: int):
        """
        Find the pair using a hash map.
        Time: O(n) average | Space: O(n)
        """
        hash_map = {}  # Up to n elements → O(n) space

        # One loop → O(n)
        # Hash lookup/insertion → O(1) average
        for i, num in enumerate(arr):
            remaining = target - num

            if remaining in hash_map:
                return [hash_map[remaining], i]

            hash_map[num] = i

        return [-1, -1]