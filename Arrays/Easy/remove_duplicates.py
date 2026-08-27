class Solution:
    def remove_duplicates(self, arr: list[int]) -> int:
        """
        Remove duplicates from a sorted array in-place.

        Time: O(n)
        Space: O(1)
        """
        if not arr:
            return 0

        # `i` points to the last unique element.
        i: int = 0

        # Scan the array using the second pointer.
        for j in range(1, len(arr)):
            if arr[j] != arr[i]:
                i += 1
                arr[i] = arr[j]

        # Number of unique elements.
        return i + 1