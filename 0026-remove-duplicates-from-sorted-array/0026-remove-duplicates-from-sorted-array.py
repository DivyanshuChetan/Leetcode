# class Solution(object):
#     def removeDuplicates(self, nums):
#         j=0
#         for i in range(1,len(nums)):
#             if nums[j]!=nums[i]:
#                 j+=1
#                 nums[j]=nums[i]
#         return j+1

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        j = 1  # Initialize a pointer to keep track of the next position for non-duplicate elements

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[j] = nums[i]
                j += 1

        return j
