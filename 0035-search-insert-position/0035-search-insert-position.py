# class Solution:
#     def searchInsert(self, nums: List[int], target: int) -> int:
        
#         s= 0
#         e= len(nums) - 1
        
#         while s <= e:
#             mid = (s + e) // 2
            
#             if nums[mid] == target:
#                 return mid
#             elif target > nums[mid]:
#                 s = mid + 1
#             else:
#                 e= mid - 1
        
#         return s
class Solution(object):
    def searchInsert(self, nums, target):
        for i in range(len(nums)):
            if(nums[i] >= target):
                return i
        return len(nums)