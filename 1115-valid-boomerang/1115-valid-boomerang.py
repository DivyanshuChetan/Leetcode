# class Solution:
#     def isBoomerang(self, points: List[List[int]]) -> bool:
#         if (
#             points[1][0] - points[0][0] == 0
#             or points[2][0] - points[1][0] == 0):
#             return True
#         slope1=(points[1][1]-points[0][1]) / (points[1][0]-points[0][0])
#         slope2=(points[2][1]-points[1][1]) / (points[2][0]-points[1][0])
#         if slope1==slope2:
#             return True
# class Solution:
#     def isBoomerang(self, points: List[List[int]]) -> bool:
#         if (
#             points[1][0] - points[0][0] == 0
#             or points[2][0] - points[1][0] == 0
#         ):
#             return True  # Two points have the same x-coordinate, forming a vertical line
        
#         slope1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0])
#         slope2 = (points[2][1] - points[1][1]) / (points[2][0] - points[1][0])

#         return slope1 != slope2  # Check if the slopes are different
class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        return (
            (points[1][0] - points[0][0]) * (points[2][1] - points[0][1])
            != (points[2][0] - points[0][0]) * (points[1][1] - points[0][1])
        )
