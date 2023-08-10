class Solution(object):
    def search(self, nums, target):

        # for i in range(len(nums)):
        #     if nums[i]==target:
        #         return i
        # return -1

        left=0
        right=len(nums)-1

        while left <= right:
            mid = (left+right) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1