class Solution:

    def spiralMatrix(self, mat: list[list[int]]) -> list[int]:
        """
        Traverse the matrix in spiral order.
        Time: O(n × m) | Space: O(n × m)
        """
        n = len(mat)
        m = len(mat[0])

        left = 0
        right = m - 1
        top = 0
        bottom = n - 1

        ans = []

        # Traverse each boundary once → O(n × m)
        while top <= bottom and left <= right:

            # Left → Right
            for i in range(left, right + 1):
                ans.append(mat[top][i])
            top += 1

            # Top → Bottom
            for i in range(top, bottom + 1):
                ans.append(mat[i][right])
            right -= 1

            # Right → Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    ans.append(mat[bottom][i])
                bottom -= 1

            # Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    ans.append(mat[i][left])
                left += 1

        return ans
