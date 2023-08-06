# class Solution(object):
#     def getConcatenation(self, nums):
#         ans=[]
#         temp=[]
#         for i in nums:
#             ans.append(i)
#         for i in ans:
#             nums.append(i)
#         # for i in temp:
#         #     ans.append(i)
#         return nums
class Solution(object):
    def getConcatenation(self, nums):
        answer = [0] * (2 * len(nums))
        j = 0       
        for i in range(len(nums)):         
            answer[i] = nums[i]           
            answer[i + len(nums)] = nums[i]
        return answer

