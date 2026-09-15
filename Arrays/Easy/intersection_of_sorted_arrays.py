class Solution:

    # Brute Force
    def findArrayIntersectionBruteForce(
        self,
        arr1: list[int],
        arr2: list[int]
    ) -> list[int]:
        """Find intersection using brute force.

        Time Complexity: O(n * m)
        Space Complexity: O(m + k)
        """
        n1, n2 = len(arr1), len(arr2)

        intersection = []
        visited = [False] * n2

        for i in range(n1):
            for j in range(n2):

                if arr1[i] == arr2[j] and not visited[j]:
                    intersection.append(arr1[i])
                    visited[j] = True
                    break

                # Arrays are sorted.
                if arr2[j] > arr1[i]:
                    break

        return intersection

    # Optimal
    def findArrayIntersection(
        self,
        arr1: list[int],
        arr2: list[int]
    ) -> list[int]:
        """Find intersection using two pointers.

        Time Complexity: O(n + m)
        Space Complexity: O(k)  # Output array.
        """
        n1, n2 = len(arr1), len(arr2)

        intersection = []

        i = j = 0

        while i < n1 and j < n2:

            if arr1[i] < arr2[j]:
                i += 1

            elif arr2[j] < arr1[i]:
                j += 1

            else:
                intersection.append(arr1[i])
                i += 1
                j += 1

        return intersection