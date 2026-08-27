class Solution:
    def is_sorted(self, n: int, arr: list[int]) -> bool:
        """
        Check whether the array is sorted in non-decreasing order.

        Time: O(n)
        Space: O(1)
        """
        # Compare each element with the previous one.
        for i in range(1, n):
            if arr[i] < arr[i - 1]:
                return False

        return True