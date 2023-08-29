class Solution(object):
    def lengthOfLastWord(self, s):
        count=0
        space=False

        for i in xrange(len(s)):
            if s[i]==" ":
                space=True
            elif s[i]!=" " and space:
                count=1
                space = False
            else:
                count +=1
        return count

        