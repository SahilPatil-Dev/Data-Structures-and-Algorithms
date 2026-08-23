class Solution:
    """
    Bubble Sort implementation.

    Best Time: O(n)
    Average/Worst Time: O(n^2)
    Space: O(1)
    """

    def bubble_sort(self, n: int, arr: list) -> list:
        """Sorts the array in ascending order."""
        for end in range(n - 1, 0, -1):
            swapped = False

            # Compare adjacent elements.
            for j in range(end):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True

            # Stop if the array is already sorted.
            if not swapped:
                break

        return arr