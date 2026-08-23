class Solution:
    """
    Insertion Sort implementation.

    Best Time: O(n)
    Average/Worst Time: O(n^2)
    Space: O(1)
    """

    def insertion_sort(self, n: int, arr: list) -> list:
        """Sorts the array in ascending order."""
        for i in range(1, n):
            current = i

            # Move the element to its correct position.
            while current > 0 and arr[current - 1] > arr[current]:
                arr[current - 1], arr[current] = (
                    arr[current],
                    arr[current - 1],
                )
                current -= 1

        return arr