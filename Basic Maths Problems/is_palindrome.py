class Solution:
    def is_palindrome(self, n: int) -> bool:
        """Checks if an integer is a palindrome using numeric reversal."""
        if n < 0:
            return False  # Negative numbers cannot be palindromes (e.g., -121 != 121-)

        original_num = n
        reversed_num = 0
        
        while n > 0:
            last_digit = n % 10
            reversed_num = (reversed_num * 10) + last_digit
            n //= 10
            
        return reversed_num == original_num
