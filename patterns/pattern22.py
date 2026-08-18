class Solution:
 def pattern22(self, n):
  for i in range(2*n-1):
   for j in range(2*n-1):
    top = i
    left = j
    right = (2*n-2) - j
    bottom = (2*n-2) - i
    print(n - min(min(top, bottom), min(left, right)), end="")
   print()