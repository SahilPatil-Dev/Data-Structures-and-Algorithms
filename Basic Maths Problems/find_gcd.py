class Solution1:
    """Calculates GCD using linear brute-force scan."""
    
    def find_gcd(self, n1: int, n2: int) -> None:
        # Time Complexity: O(min(n1, n2))
        # It can loop up to min(n1, n2) times.
        for i in range(min(n1, n2), 0, -1):
            if n1 % i == 0 and n2 % i == 0:
                print(i)
                break


class Solution2:
    """Calculates GCD using the Euclidean algorithm."""
    
    def find_gcd(self, a: int, b: int) -> None:
        # Time Complexity: O(log(min(a, b)))
        # The numbers shrink by half very quickly.
        while a > 0 and b > 0:
            if a > b:
                a %= b
            else:
                b %= a
                
        print(a if b == 0 else b)
