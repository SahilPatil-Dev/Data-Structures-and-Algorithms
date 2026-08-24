from typing import List


class Solution:
    def merge(self, arr: List[int], low: int, mid: int, high: int) -> None:
        """
        Merge two sorted halves.

        Time: O(n)
        Space: O(n)
        """
        left = low
        right = mid + 1
        temp = []

        # Compare elements from both halves.
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining left-half elements.
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining right-half elements.
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy sorted elements back into the array.
        for i in range(len(temp)):
            arr[low + i] = temp[i]

    def mergeSort(self, arr: List[int], low: int, high: int) -> None:
        """
        Sort the array using merge sort.

        Time: O(n log n)
        Space: O(n)
        """
        # Stop when there is one or zero elements.
        if low >= high:
            return

        # Find the middle index.
        mid = (low + high) // 2

        # Sort the left half.
        self.mergeSort(arr, low, mid)

        # Sort the right half.
        self.mergeSort(arr, mid + 1, high)

        # Merge both sorted halves.
        self.merge(arr, low, mid, high)

    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sort the given array in ascending order.

        Time: O(n log n)
        Space: O(n)
        """
        self.mergeSort(nums, 0, len(nums) - 1)
        return nums