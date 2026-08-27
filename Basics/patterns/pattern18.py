class Solution:
 def pattern18(self, n):
  for i in range(n):
   start = ord("E") - i
   end = ord("E")
   for ch in range(start, end+1):
    print(chr(ch), end=" ")
    
   print()