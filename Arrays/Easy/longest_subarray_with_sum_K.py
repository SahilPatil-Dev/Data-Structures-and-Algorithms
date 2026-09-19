class Solution:

    # Brute Force
    def LongestSubArrayWithSumK_brute_force(arr: list, k: int):
        """
        Find the length of the longest subarray with sum equal to k.

        Approach:
        - Generate every possible subarray.
        - Calculate its sum.
        - If the sum is k, update the maximum length.

        Time Complexity:
            O(n³)

        Space Complexity:
            O(1)
        """
        n = len(arr)
        maxLen = 0

        for i in range(n):
            for j in range(i, n):
                asum = 0

                for x in range(i, j + 1):
                    asum += arr[x]

                if asum == k:
                    maxLen = max(maxLen, j - i + 1)

        return maxLen


    # Better
    def LongestSubArrayWithSumK_better(arr: list, k: int):
        """
        Find the length of the longest subarray with sum equal to k.

        Approach:
        - Generate all subarrays using two loops.
        - Maintain a running sum instead of calculating the sum
          again for every subarray.

        Time Complexity:
            O(n²)

        Space Complexity:
            O(1)
        """
        n = len(arr)
        maxLen = 0

        for i in range(n):
            asum = 0

            for j in range(i, n):
                asum += arr[j]

                if asum == k:
                    maxLen = max(maxLen, j - i + 1)

        return maxLen


    # Optimal - Sliding Window
    def LongestSubArrayWithSumK_optimal(arr: list, k: int):
        """
        Find the longest subarray with sum equal to k using
        the sliding window technique.

        Note:
            This approach works when all array elements are
            non-negative (0 or positive).

        Approach:
        - Expand the window using `right`.
        - If the sum becomes greater than k, move `left`
          to shrink the window.
        - When the sum equals k, update the maximum length.

        Time Complexity:
            O(n)

        Space Complexity:
            O(1)
        """
        left = 0
        right = 0
        maxLen = 0
        asum = 0
        n = len(arr)

        while right < n:

            # Add current element to the window
            asum += arr[right]

            # Shrink window if sum exceeds k
            while left <= right and asum > k:
                asum -= arr[left]
                left += 1

            # Check if current window has sum k
            if asum == k:
                maxLen = max(maxLen, right - left + 1)

            right += 1

        return maxLen


    # Optimal - Prefix Sum + Hashing
    def LongestSubArrayWithSumK_prefix_sum(arr: list, k: int):
        """
        Find the longest subarray with sum equal to k using
        prefix sum and hashing.

        Approach:
        - Maintain the current prefix sum.
        - If:
              current_sum - k
          exists in the hash map, then a subarray with sum k
          exists between that previous index and the current index.
        - Store only the first occurrence of each prefix sum
          because it gives the longest possible subarray.

        This approach works with:
        - Positive numbers
        - Zero
        - Negative numbers

        Time Complexity:
            O(n) average

        Space Complexity:
            O(n)
        """
        prefix_sum = {}
        asum = 0
        maxLen = 0

        for i in range(len(arr)):
            asum += arr[i]

            # Subarray from index 0 to i
            if asum == k:
                maxLen = max(maxLen, i + 1)

            # Check whether a previous prefix sum exists
            rem = asum - k

            if rem in prefix_sum:
                length = i - prefix_sum[rem]
                maxLen = max(maxLen, length)

            # Store only the first occurrence
            if asum not in prefix_sum:
                prefix_sum[asum] = i

        return maxLen