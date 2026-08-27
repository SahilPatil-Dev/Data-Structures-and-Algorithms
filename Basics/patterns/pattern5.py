class Solution:
 def pattern5(self, n):
  for i in range(n):
   for j in range(n-i):
    print("*", end="")
   print()
                                         