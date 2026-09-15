class Solution:

    # Brute Force
    def sortedArrayBruteForce(
        self,
        arr1: list[int],
        arr2: list[int]
    ) -> list[int]:
        """Find union of two sorted arrays using a set.

        Time Complexity: O((n + m) log(n + m))
        Space Complexity: O(n + m)
        """
        unique = set()

        for value in arr1:
            unique.add(value)

        for value in arr2:
            unique.add(value)

        return sorted(unique)

    # Optimal
    def sortedArray(
        self,
        arr1: list[int],
        arr2: list[int]
    ) -> list[int]:
        """Find union of two sorted arrays using two pointers.

        Time Complexity: O(n + m)
        Space Complexity: O(n + m)  # Output array.
        """
        n1, n2 = len(arr1), len(arr2)
        union_arr = []

        i = j = 0

        while i < n1 and j < n2:

            if arr1[i] < arr2[j]:
                value = arr1[i]
                i += 1

            elif arr2[j] < arr1[i]:
                value = arr2[j]
                j += 1

            else:
                value = arr1[i]
                i += 1
                j += 1

            # Avoid duplicates.
            if not union_arr or union_arr[-1] != value:
                union_arr.append(value)

        # Remaining elements of arr1.
        while i < n1:
            if not union_arr or union_arr[-1] != arr1[i]:
                union_arr.append(arr1[i])
            i += 1

        # Remaining elements of arr2.
        while j < n2:
            if not union_arr or union_arr[-1] != arr2[j]:
                union_arr.append(arr2[j])
            j += 1

        return union_arr