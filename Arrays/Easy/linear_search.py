class Solution:

    def linearSearch(self, arr: list[int], n: int, a: int) -> int:
        """Find the index of an element using linear search.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        for i in range(n):
            if arr[i] == a:
                return i

        return -1