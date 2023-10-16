class Solution:
    def isPrime(self, num):
        a = []
        if num <= 1: return False
        for i in range(2, isqrt(num) + 1):
            if not num % i:
                a.append(i)
        return not a
    
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j or i + j == len(nums) - 1:
                    print(nums[i][j])
                    a.append(nums[i][j])
                    print(a)
        b = []
        for ele in a:
            if self.isPrime(ele):
                b.append(ele)
        print(b)
        return max(b) if b else 0
        