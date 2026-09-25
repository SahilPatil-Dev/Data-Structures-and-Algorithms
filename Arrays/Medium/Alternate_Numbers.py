class Solution:

    def alternateNumbers(self, arr: list):
        """
        Rearrange positive and negative numbers alternately.
        Extra elements are added at the end.
        Time: O(n) | Space: O(n)
        """
        pos = []
        neg = []

        # Separate positive and negative elements → O(n)
        for num in arr:
            if num > 0:
                pos.append(num)
            else:
                neg.append(num)

        # More positive elements
        if len(pos) > len(neg):

            # Alternate until negatives are exhausted → O(n)
            for i in range(len(neg)):
                arr[2 * i] = pos[i]
                arr[2 * i + 1] = neg[i]

            # Append remaining positives
            index = len(neg) * 2

            for i in range(len(neg), len(pos)):
                arr[index] = pos[i]
                index += 1

        # More or equal negative elements
        else:

            # Alternate until positives are exhausted → O(n)
            for i in range(len(pos)):
                arr[2 * i] = pos[i]
                arr[2 * i + 1] = neg[i]

            # Append remaining negatives
            index = len(pos) * 2

            for i in range(len(pos), len(neg)):
                arr[index] = neg[i]
                index += 1

        return arr