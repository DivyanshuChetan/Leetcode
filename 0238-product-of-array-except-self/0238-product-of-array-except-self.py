class Solution(object):
    def productExceptSelf(self, nums):
        n=len(nums)
        left_product=1
        right_product=1
        answer=[1]*n
 
        for i in range(n):
            answer[i]*=left_product
            left_product*=nums[i]
        
        for i in range(n-1,-1,-1):
            answer[i]*=right_product
            right_product*=nums[i]
        
        return answer