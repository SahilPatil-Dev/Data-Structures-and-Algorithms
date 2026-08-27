class Solution:
 def pattern4(self, n):
  for i in range(1,n):
   for j in range(i):
    print(i, end="")
   print()
                                         