class Solution:
    def ReverseNumber(self, n):
        NewNo=0
        while n>0:
            ld = n % 10
            NewNo = (NewNo * 10) + ld
            n //= 10
        return NewNo
