class Solution:
    def print_n_to_1_backtracking(self, i, n):
        """Print numbers from n to 1 using backtracking."""
        if i > n:
            return

        self.print_n_to_1_backtracking(i + 1, n)
        print(i)  # Backtracking 

# Time: O(n)
# Space: O(n) - recursion stack