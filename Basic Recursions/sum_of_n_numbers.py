class Solution:

    # Parameterized Recursion
    def sum_parameterized_recursion(
        self,
        n: int,
        current_sum: int = 0
    ) -> None:
        # Time: O(n)
        # Space: O(n) - recursive call stack

        if n < 1:
            print(current_sum)
            return

        self.sum_parameterized_recursion(n - 1, current_sum + n)

    # Functional Recursion
    def sum_functional_recursion(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n) - recursive call stack

        if n == 0:
            return 0

        return n + self.sum_functional_recursion(n - 1) 