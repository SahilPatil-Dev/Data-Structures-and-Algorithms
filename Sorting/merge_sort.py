class Solution:
    def merge(self, arr: list, low: int, mid: int, high: int) -> None:
        """
        Merge two sorted halves of arr in-place.

        Time: O(n), Space: O(n)
        """
        left = low
        right = mid + 1
        temp = []

        # Merge both halves into temp.
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        # Add remaining elements from the left half.
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Add remaining elements from the right half.
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy merged elements back into arr.
        for i in range(len(temp)):
            arr[low + i] = temp[i]

    def mergeSort(self, arr: list, low: int, high: int) -> None:
        """
        Sort arr[low:high+1] using merge sort.

        Time: O(n log n), Space: O(n)
        """
        if low >= high:
            return

        # Find the middle index.
        mid = (low + high) // 2

        # Sort both halves.
        self.mergeSort(arr, low, mid)
        self.mergeSort(arr, mid + 1, high)

        # Merge the sorted halves.
        self.merge(arr, low, mid, high)