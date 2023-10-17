class Solution:
    def isWinner(self, player1: List[int], player2: List[int]) -> int:
        def f(player):
            n=len(player)
            if n==1:
                return player[0]
            a,b=player[0:2]
            answ=player[0] + player[1] + (player[0]==10)*player[1]
            for x in player[2:]:
                answ+=x + (max(a,b)==10)*x
                a,b=b,x
            return answ
        p1=f(player1)
        p2=f(player2)
        if p1==p2:
            return 0
        if p1<p2:
            return 2
        return 1