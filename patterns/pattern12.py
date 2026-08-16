class Solution:
 def pattern12(self, n):
  space = 2*(n-1)
  
  for i in range(1,n+1):
   
   #numbers
   for x in range(1,i+1):
    print(x, end="")
   
   #spaces
   for y in range(1,space+1):
    print(" ", end="")
    
   #numbers
   for z in range(i,0,-1):
    print(z, end="")
    
   space -= 2
   
   print()