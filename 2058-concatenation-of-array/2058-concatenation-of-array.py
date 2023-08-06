class Solution(object):
    def getConcatenation(self, nums):
        ans=[]
        temp=[]
        for i in nums:
            ans.append(i)
        for i in ans:
            nums.append(i)
        # for i in temp:
        #     ans.append(i)
        return nums