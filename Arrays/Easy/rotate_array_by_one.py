class Solution:
    def rotate_array_by_one(self, arr: list[int]) -> list[int]:
        """
        Rotate the array to the left by one position.
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        if not arr:
            return arr

        temp = arr[0]

        for i in range(1, len(arr)):
            arr[i - 1] = arr[i]

        arr[-1] = temp
        return arr