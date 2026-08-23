class Solution:
    """
    Selection Sort implementation.

    Time: O(n^2)
    Space: O(1)
    """

    def selection_sort(self, n: int, arr: list) -> list:
        """Sorts the array in ascending order."""
        for i in range(n - 1):
            min_index = i

            # Find the minimum element.
            for j in range(i + 1, n):
                if arr[j] < arr[min_index]:
                    min_index = j

            # Swap minimum with current element.
            arr[i], arr[min_index] = arr[min_index], arr[i]

        return arr