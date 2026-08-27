import sys

class Solution:
    def second_largest(self, n: int, arr: list[int]) -> int:
        """
        Return the second largest distinct element.

        Time: O(n)
        Space: O(1)
        """
        largest: int = arr[0]
        second_largest: int = -sys.maxsize

        for i in range(1, n):
            if arr[i] > largest:
                second_largest = largest
                largest = arr[i]
            elif arr[i] < largest and arr[i] > second_largest:
                second_largest = arr[i]

        return second_largest

    def second_smallest(self, n: int, arr: list[int]) -> int:
        """
        Return the second smallest distinct element.

        Time: O(n)
        Space: O(1)
        """
        smallest: int = arr[0]
        second_smallest: int = sys.maxsize

        for i in range(1, n):
            if arr[i] < smallest:
                second_smallest = smallest
                smallest = arr[i]
            elif arr[i] > smallest and arr[i] < second_smallest:
                second_smallest = arr[i]

        return second_smallest

    def getSecondOrderElements(self, n: int, arr: list[int]) -> list[int]:
        """
        Return [second largest, second smallest].

        Time: O(n)
        Space: O(1)
        """
        return [
            self.second_largest(n, arr),
            self.second_smallest(n, arr),
        ]