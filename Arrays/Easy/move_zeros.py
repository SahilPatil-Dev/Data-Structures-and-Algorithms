class Solution:

    def moveZerosBruteForce(self, n: int, a: list[int]) -> list[int]:
        """
        Brute-force approach:
        Collect non-zero elements, then fill the remaining
        positions with zeros.

        Time Complexity: O(n)
        Space Complexity: O(n)
        """
        temp = []

        # Store all non-zero elements.
        for num in a:
            if num != 0:
                temp.append(num)

        # Copy non-zero elements back.
        for i in range(len(temp)):
            a[i] = temp[i]

        # Fill remaining positions with zeros.
        for i in range(len(temp), n):
            a[i] = 0

        return a

    def moveZeros(self, n: int, a: list[int]) -> list[int]:
        """
        Optimal two-pointer approach:
        Moves zeros to the end in-place while preserving
        the relative order of non-zero elements.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Find the first zero.
        j = -1

        for i in range(n):
            if a[i] == 0:
                j = i
                break

        # No zeros present.
        if j == -1:
            return a

        # Place each non-zero element at the next available
        # zero position.
        for i in range(j + 1, n):
            if a[i] != 0:
                a[i], a[j] = a[j], a[i]
                j += 1

        return a