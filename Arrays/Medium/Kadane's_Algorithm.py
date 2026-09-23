class Solution:

    # Brute Force
    def MaximumSubArraySum_brute_force(arr: list):
        """
        Generate every subarray and calculate its sum.
        Time: O(n³) | Space: O(1)
        """
        n = len(arr)
        maxSum = 0

        # Choose starting index → O(n)
        for i in range(n):

            # Choose ending index → O(n)
            for j in range(i, n):
                asum = 0

                # Calculate subarray sum → O(n)
                for k in range(i, j + 1):
                    asum += arr[k]

                maxSum = max(maxSum, asum)

        return maxSum


    # Better
    def MaximumSubArraySum_better(arr: list):
        """
        Generate subarrays with a running sum.
        Time: O(n²) | Space: O(1)
        """
        n = len(arr)
        maxSum = 0

        # Two nested loops → O(n²)
        for i in range(n):
            asum = 0

            for j in range(i, n):
                # Reuse previous sum instead of another loop
                # → O(1) per iteration
                asum += arr[j]

                maxSum = max(maxSum, asum)

        return maxSum


    # Optimal - Kadane's Algorithm
    def MaximumSubArraySum_optimal(arr: list):
        """
        Find the maximum subarray sum using Kadane's Algorithm.
        Time: O(n) | Space: O(1)
        """
        asum = 0
        maxSum = arr[0]

        # One loop → O(n)
        for num in arr:
            asum += num

            # Keep the best subarray ending here
            maxSum = max(maxSum, asum)

            # Negative sum can only reduce a future subarray.
            # Start fresh from the next element.
            if asum < 0:
                asum = 0

        return maxSum