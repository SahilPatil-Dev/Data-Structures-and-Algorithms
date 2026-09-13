class Solution:

    # Brute force
    def left_rotate1(self, arr: list[int], n: int, d: int) -> list[int]:
        """
        Rotate the array to the left by d positions using extra space.

        Time Complexity: O(n)
        Space Complexity: O(d)
        """
        if n == 0:
            return arr

        d %= n
        temp = arr[:d]

        for i in range(d, n):
            arr[i - d] = arr[i]

        for i in range(d):
            arr[n - d + i] = temp[i]

        return arr

    def reverse(self, arr: list[int], start: int, end: int) -> None:
        """Reverse the elements between start and end indices."""
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1

    # Optimal approach
    def left_rotate2(self, arr: list[int], n: int, d: int) -> list[int]:
        """
        Rotate the array to the left by d positions using reversal.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if n == 0:
            return arr

        d %= n

        self.reverse(arr, 0, d - 1)
        self.reverse(arr, d, n - 1)
        self.reverse(arr, 0, n - 1)

        return arr