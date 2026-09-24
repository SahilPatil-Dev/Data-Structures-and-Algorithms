class Solution:

    # Brute Force
    def leaders_brute_force(arr: list):
        """
        Find elements greater than every element to their right.
        Time: O(n²) | Space: O(n)
        """
        n = len(arr)
        ans = []

        # For every element → O(n)
        for i in range(n):
            leader = True

            # Check all elements to its right → O(n)
            for j in range(i + 1, n):
                if arr[j] >= arr[i]:
                    leader = False
                    break

            if leader:
                ans.append(arr[i])  # At most n elements → O(n) space

        # Optional: required when output must be sorted
        ans.sort()  # O(n log n)

        return ans


    # Optimal
    def leaders_optimal(arr: list):
        """
        Find leaders by scanning from right to left.
        Time: O(n log n)* | Space: O(n)
        """
        n = len(arr)
        ans = []

        max_right = arr[-1]

        # Last element is always a leader.
        ans.append(max_right)

        # One reverse traversal → O(n)
        for i in range(n - 2, -1, -1):

            # Current element must be greater than all
            # elements seen on its right.
            if arr[i] > max_right:
                ans.append(arr[i])

            # Keep track of maximum on the right → O(1)
            max_right = max(max_right, arr[i])

        # Required only if output must be in sorted order.
        ans.sort()  # O(n log n)

        return ans