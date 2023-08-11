class Solution(object):
    def decompressRLElist(self, nums):
        # arr=[]
        # for i in range(len(nums)):
        #     freq=0
        #     val=0
        #     freq=nums[2*i] and val=nums[2*i+1]    
        #     arr.append(freq,val)

        answer = []
        for i in range(len(nums)//2):
            answer += nums[2*i]*[nums[2*i+1]]
        return answer