class Solution:
    def isUgly(self, n: int) -> bool:
        if n==0:
            return 
        if n==1:
            return True
        # if n%2==0 or n%3==0 or n%5==0:
        #     return True
        for i in (2,3,5):
            while n%i==0:
                n//=i
        return n==1