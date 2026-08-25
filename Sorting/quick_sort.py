class Solution:
    def Sort(self, arr: list, low: int, high: int) -> int:
        """
        Partitions the array around the first element as pivot.

        Time: O(n) average for one partition
        Space: O(1)
        """
        pivot = arr[low]
        i = low
        j = high

        while i < j:
            # Move i right while elements are <= pivot
            while i <= high and arr[i] <= pivot:
                i += 1

            # Move j left while elements are > pivot
            while j >= low and arr[j] > pivot:
                j -= 1

            # Swap elements if pointers haven't crossed
            if i < j:
                arr[i], arr[j] = arr[j], arr[i]

        # Place pivot in its correct position
        arr[low], arr[j] = arr[j], arr[low]

        return j

    def quickSort(self, arr: list, low: int, high: int) -> list:
        """
        Recursively sorts the array using Quick Sort.

        Average Time: O(n log n)
        Worst Time:   O(n²)
        Space:        O(log n) average, O(n) worst case (recursion stack)
        """
        if low < high:
            partitionIndex = self.Sort(arr, low, high)

            # Sort left and right partitions
            self.quickSort(arr, low, partitionIndex - 1)
            self.quickSort(arr, partitionIndex + 1, high)

        return arr