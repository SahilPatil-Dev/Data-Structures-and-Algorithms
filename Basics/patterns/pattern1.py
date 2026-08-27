class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

# Output pattern for n = 4:
# ****
# ****
# ****
# ****