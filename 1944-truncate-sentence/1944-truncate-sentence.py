class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        x=list(s.split())
        y=[]
        y+=x[0:k]
        z=' '.join(y)
        return z