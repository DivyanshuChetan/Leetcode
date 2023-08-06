class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in range(len(stones)):
            for j in range(len(jewels)):
                if stones[i]==jewels[j]:
                    count+=1
        return count