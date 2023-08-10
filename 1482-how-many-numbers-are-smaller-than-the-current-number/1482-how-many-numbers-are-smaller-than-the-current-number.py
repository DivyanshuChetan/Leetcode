class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        
#         arr=[]
#         for i in range(len(nums)):
#             count=0
#             for j in range(len(nums)):
#                 if i!=j and nums[j] < nums[i]:
#                     count+=1
#             arr.append(count)
#         return arr
        
        l1 = sorted(nums)
        return [l1.index(i) for i in nums]