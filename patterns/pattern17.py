class Solution:
 def pattern17(self, n):
  for i in range(n):
   
   #Spaces
   print(" "*(n-i-1), end="")
   
   breakpoint = (2*i+1) // 2
   ch = ord("A")
   #Letters
   for j in range(1, (2*i+2)):
    print(chr(ch), end="")
    
    ch= ch + 1 if j<=breakpoint else ch - 1
    
   print()