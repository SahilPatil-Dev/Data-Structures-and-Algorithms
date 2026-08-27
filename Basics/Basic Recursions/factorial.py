class Solution:

    # Parameterized Recursion
    def factorial_parameterized_recursion(
        self,
        n: int,
        current_fact: int = 1
    ) -> None:
        # Time: O(n)
        # Space: O(n) - recursive call stack

        if n < 1:
            print(current_fact)
            return

        self.factorial_parameterized_recursion(
            n - 1,
            current_fact * n
        )

    # Functional Recursion
    def factorial_functional_recursion(self, n: int) -> int:
        # Time: O(n)
        # Space: O(n) - recursive call stack

        if n < 1:
            return 1

        return n * self.factorial_functional_recursion(n - 1)