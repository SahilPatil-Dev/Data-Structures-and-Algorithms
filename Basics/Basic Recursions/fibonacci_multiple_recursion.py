class Solution:
    def fibonacci_multiple_recursion(self, n: int) -> int:
        """Calculates the nth Fibonacci number using naive recursion."""
        if n <= 1:
            return n
        
        last = self.fibonacci_multiple_recursion(n - 1)
        slast = self.fibonacci_multiple_recursion(n - 2)
        
        return last + slast
