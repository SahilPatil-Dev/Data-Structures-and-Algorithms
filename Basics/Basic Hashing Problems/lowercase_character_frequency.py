"""
Count the frequency of lowercase English characters
using a frequency array.

Time Complexity:
    O(N + Q)

Space Complexity:
    O(26) = O(1)
"""


class CharacterFrequency:
    def count_frequency(self, s, queries):
        # Frequency array for 26 lowercase letters
        freq = [0] * 26

        # Precompute character frequencies
        for ch in s:
            index = ord(ch) - ord('a')
            freq[index] += 1

        # Fetch frequency for each query
        for ch in queries:
            index = ord(ch) - ord('a')
            print(freq[index])
