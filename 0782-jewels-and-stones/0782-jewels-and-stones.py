# class Solution(object):
#     def numJewelsInStones(self, jewels, stones):
#         count=0
#         for i in stones:
#             for j in jewels:
#                 if i==j:
#                     count+=1
#         return count

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        count=0
        for i in stones:
            if i in jewels:
                count+=1
        return count