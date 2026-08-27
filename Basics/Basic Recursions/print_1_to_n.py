class Solution:
    def print_1_to_n(self, i, n):
        """Print numbers from 1 to n using normal recursion."""
        if i > n:
            return

        print(i)
        self.print_1_to_n(i + 1, n)

# Time: O(n)
# Space: O(n) - recursion stack