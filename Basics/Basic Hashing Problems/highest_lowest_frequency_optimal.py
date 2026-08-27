"""
Find the element with the highest and lowest frequency
using a dictionary (hash map).

Time Complexity:
    O(N) average

Space Complexity:
    O(N)
"""


class FrequencyCounter:
    def find_highest_lowest(self, arr):
        # Dictionary stores:
        # element -> frequency
        freq_map = {}

        # Precompute frequencies
        for num in arr:
            freq_map[num] = freq_map.get(num, 0) + 1

        # Initialize maximum and minimum frequencies
        max_freq = 0
        min_freq = len(arr)

        max_element = 0
        min_element = 0

        # Find highest and lowest frequency elements
        for element, count in freq_map.items():

            # Update highest frequency
            if count > max_freq:
                max_freq = count
                max_element = element

            # Update lowest frequency
            if count < min_freq:
                min_freq = count
                min_element = element

        print("The highest frequency element is:", max_element)
        print("The lowest frequency element is:", min_element)
