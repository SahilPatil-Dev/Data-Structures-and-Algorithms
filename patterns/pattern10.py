class Solution:
    def pattern10(self, n):
        for i in range(1,2*n):
            stars = i if i <= n else (2*n-i)
            for x in range(stars):
                print("*", end="")
            print()