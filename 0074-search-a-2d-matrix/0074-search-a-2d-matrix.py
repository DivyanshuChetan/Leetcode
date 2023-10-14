class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix)-1

        while left <= right:
            mid = (left+right)//2
            
            if target < matrix[mid][0]:
                right = mid-1
            elif target > matrix[mid][-1]:
                left = mid+1
            else:
                return target in matrix[mid]
                

             