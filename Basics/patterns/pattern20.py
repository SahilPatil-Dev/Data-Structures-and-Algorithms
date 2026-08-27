class Solution:
 def pattern20(self, n):
  spaces = 2*n-2
  
  for i in range(1,2*n):
   Stars = i if i <= n else 2*n-i
   
   #Stars
   for x in range(Stars):
    print("*", end="")
   
   #Spaces
   for y in range(spaces):
    print(" ", end="")
   
   #Stars
   for z in range(Stars):
    print("*", end="")
    
   spaces += -2 if i < n else 2
    
   print()