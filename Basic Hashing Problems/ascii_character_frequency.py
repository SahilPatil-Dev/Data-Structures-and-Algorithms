"""
Count the frequency of ASCII characters
using a frequency array.

Time Complexity:
    O(N + Q)

Space Complexity:
    O(256) = O(1)
"""


class ASCIICharacterFrequency:
    def count_frequency(self, s, queries):
        # Frequency array for ASCII characters
        freq = [0] * 256

        # Precompute character frequencies
        for ch in s:
            freq[ord(ch)] += 1

        # Fetch frequency for each query
        for ch in queries:
            print(freq[ord(ch)])