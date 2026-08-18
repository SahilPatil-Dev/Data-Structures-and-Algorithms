class Solution:
    def is_armstrong(self, n: int) -> bool:
        """Checks if an integer is an Armstrong (narcissistic) number."""
        # Negative numbers cannot be Armstrong numbers
        if n < 0:
            return False

        original_num = n
        num_digits = len(str(n))
        digit_sum = 0

        while n > 0:
            last_digit = n % 10
            digit_sum += last_digit ** num_digits
            n //= 10

        return digit_sum == original_num
