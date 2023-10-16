class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        maxi2=maxi=0
        for i in range(len(nums)): maxi2=max(maxi2,max(nums[i]))
        res=[0 if (i&1==0 and i!=2) or i==1 else 1 for i in range(maxi2+1) ]
        for i in range(3,maxi2+1,2):
            for j in range(i*i,maxi2+1,i): res[j]=0
            
        for i in [r[i] for i, r in enumerate(nums)]:
            if res[i]==1: maxi=max(maxi,i)
        for i in [r[~i] for i, r in enumerate(nums)]:
            if res[i]==1: maxi=max(maxi,i)
        return maxi