class Solution:
    def pattern8(self, n):
        for i in range(n):
            # Spaces
            for x in range(i):
                print(" ", end="")

            # Stars
            for y in range(2*n-2*i-1):
                print("*", end="")

            print()