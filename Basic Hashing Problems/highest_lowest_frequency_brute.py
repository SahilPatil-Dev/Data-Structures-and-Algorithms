"""
Find the element with the highest and lowest frequency
using the brute-force approach.

Time Complexity:
    O(N^2)

Space Complexity:
    O(N)
"""


class FrequencyCounter:
    def find_highest_lowest(self, arr):
        n = len(arr)

        # Keep track of elements whose frequency is already counted
        visited = [False] * n

        # Variables for maximum frequency
        max_freq = 0
        max_element = 0

        # Variables for minimum frequency
        min_freq = n
        min_element = 0

        # Check every element
        for i in range(n):

            # Skip if this element was already counted
            if visited[i]:
                continue

            # Count current element
            count = 1

            # Compare with remaining elements
            for j in range(i + 1, n):
                if arr[i] == arr[j]:
                    visited[j] = True
                    count += 1

            # Update maximum frequency
            if count > max_freq:
                max_freq = count
                max_element = arr[i]

            # Update minimum frequency
            if count < min_freq:
                min_freq = count
                min_element = arr[i]

        print("The highest frequency element is:", max_element)
        print("The lowest frequency element is:", min_element)

