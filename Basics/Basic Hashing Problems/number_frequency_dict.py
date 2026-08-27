"""
Count the frequency of numbers using a dictionary.

Time Complexity:
    O(N + Q) average

Space Complexity:
    O(N)
"""


class FrequencyCounter:
    def count_frequency(self, arr, queries):
        # Dictionary stores:
        # number -> frequency
        freq = {}

        # Precompute frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Fetch frequency for each query
        for number in queries:
            print(freq.get(number, 0))
