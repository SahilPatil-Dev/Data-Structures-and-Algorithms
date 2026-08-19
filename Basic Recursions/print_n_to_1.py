class Solution:
    def print_n_to_1(self, n):
        """Print numbers from n to 1 using normal recursion."""
        if n == 0:
            return

        print(n)
        self.print_n_to_1(n - 1)

# Time: O(n)
# Space: O(n) - recursion stack