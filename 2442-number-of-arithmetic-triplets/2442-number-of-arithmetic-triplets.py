class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        count=0
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        count+=1
        return count                