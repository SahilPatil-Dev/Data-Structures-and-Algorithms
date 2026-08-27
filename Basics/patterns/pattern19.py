class Solution:
 def pattern19(self,n):
    # 1. Top Half
    iniS = 0
    for i in range(n, 0, -1):
        # Stars + Spaces + Stars
        print("*" * i + " " * iniS + "*" * i)
        iniS += 2

    # 2. Bottom Half (The specific C++ code visible on your screen)
    iniS = 2 * n - 2
    for i in range(1, n + 1):
        # Stars + Spaces + Stars
        print("*" * i + " " * iniS + "*" * i)
        iniS -= 2

