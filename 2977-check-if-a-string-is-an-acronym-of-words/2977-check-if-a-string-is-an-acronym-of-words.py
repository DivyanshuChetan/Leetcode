class Solution(object):
    def isAcronym(self, words, s):
        res=[]
        
        for i in words:
            res.append(i[0])
        p=''.join(res)
        if p==s:
            return True
        return False