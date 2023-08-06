class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        arr=[]
        for i in range(len(candies)):
            if candies[i]+extraCandies>=max(candies):
                arr.append(True)
            else:
                arr.append(False)
        return arr
# class Solution(object):
#     def kidsWithCandies(self, candies, extraCandies):
#         arr = []
#         max_candies = max(candies)

#         for i in range(len(candies)):
#             arr.append(candies[i] + extraCandies >= max_candies)

#         return arr
