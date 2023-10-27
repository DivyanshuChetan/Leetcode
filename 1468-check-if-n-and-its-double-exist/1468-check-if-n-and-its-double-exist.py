class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        m = 0
        n = 0
        for i in arr:
            n=0
            for j in arr:
                if m==n:
                    n = n+1
                    continue
                if i==2*j:
                    return True
                n = n+1
            m = m+1        
        return False