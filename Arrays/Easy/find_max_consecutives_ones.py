class Solution:

    def findMaxConsecutiveOnes(self, arr: list, n: int):
        """
        Find the maximum number of consecutive 1s.

        Time Complexity: O(n)
        Space Complexity: O(1)
        """

        max1 = 0
        cnt = 0

        # Traverse the array
        for i in arr:
            if i == 1:
                cnt += 1
                max1 = max(max1, cnt)
            else:
                cnt = 0

        return max1