class Solution:

    def rearrangeArray(self, nums: list):
        """
        Rearrange positive and negative numbers alternately.
        Time: O(n) | Space: O(n)
        """
        n = len(nums)
        ans = [0] * n

        pos_index = 0
        neg_index = 1

        # One pass through the array → O(n)
        for num in nums:

            if num > 0:
                # Positives go to even indices:
                # 0, 2, 4, ...
                ans[pos_index] = num
                pos_index += 2

            else:
                # Negatives go to odd indices:
                # 1, 3, 5, ...
                ans[neg_index] = num
                neg_index += 2

        return ans