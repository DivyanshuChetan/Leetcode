class Solution(object):
    def lengthOfLastWord(self, s):
        space=False
        count=0
        
        for i in s:
            if i==" ":
                space=True
            elif i!=" " and space==True:
                count=1
                space=False
            else:
                count+=1
        return count