class Solution:
 def pattern7(self, n):
  for i in range(n):
   # Spaces
   for x in range(n-i-1):
    print(" ", end="")
   # Stars
   for y in range(2*i+1):
    print("*", end="")
   print()
                                     