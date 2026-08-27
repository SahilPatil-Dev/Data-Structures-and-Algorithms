"""
Count the frequency of numbers using a frequency array.

Time Complexity:
    O(N + Q)

Space Complexity:
    O(K), where K is the size of the frequency array.
"""


class FrequencyCounter:
    def count_frequency(self, arr, queries):
        # Create frequency array for numbers from 0 to 12
        freq = [0] * 13

        # Precompute frequencies
        for num in arr:
            freq[num] += 1

        # Fetch frequency for each query
        for number in queries:
            print(freq[number])
