import math


class Solution:
    def print_divisors(self, n: int) -> None:
        """Prints all divisors of a given integer n."""
        for i in range(1, n + 1):
            if n % i == 0:
                print(i, end=",")

# Optimized version to print divisors in sorted order without duplicates

class Solution:
    def printDivisions(self, n: int) -> None:
        """Finds and prints all divisors of an integer n in ascending order."""
        bucket = []
        
        # Loop up to the square root of n
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                bucket.append(i)          # Small divisor
                if n // i != i:
                    bucket.append(n // i) # Complementary large divisor
                    
        bucket.sort()
        print(*bucket)