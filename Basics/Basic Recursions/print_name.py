class Solution:
    def print_name(self, i, n, name):
        """Print the given name n times using recursion."""
        if i > n:
            return

        print(name)
        self.print_name(i + 1, n, name)

# Time: O(n)
# Space: O(n) - recursion stack