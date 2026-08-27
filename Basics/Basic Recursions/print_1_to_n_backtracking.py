class Solution:
    def print_1_to_n_backtracking(self, n):
        """Print numbers from 1 to n using backtracking."""
        if n == 0:
            return

        self.print_1_to_n_backtracking(n - 1)
        print(n)  # Backtracking

# Time: O(n)
# Space: O(n) - recursion stack