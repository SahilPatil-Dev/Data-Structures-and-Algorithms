class Solution:
    def pattern9(self, n):
        for i in range(n):
            # Spaces
            for x in range(n - i - 1):
                print(" ", end="")

            # Stars
            for y in range(2 * i + 1):
                print("*", end="")
            
            print()
            
        for j in range(n):   
            # Spaces
            for x in range(j):
                print(" ", end="")
            
            # Stars  
            for y in range(2*n-2*j-1):
                print("*", end="")

            print()