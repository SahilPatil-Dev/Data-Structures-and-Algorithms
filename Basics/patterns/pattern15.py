class Solution:
 def pattern15(self, n):
  for i in range(1, n+1):
   for j in range(n-i):
    print(chr(ord("A")+j),end=" ")
   print()