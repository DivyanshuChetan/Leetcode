class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        a=Counter(deck)
        w=list(set(a.values()))
        div=0
        if len(w)==1:
            div=w[0]
        else:
            div=math.gcd(w[0],w[1])
           
            for i in range(1,len(w)-1):
                div=math.gcd(div,w[i+1])
        return div>1