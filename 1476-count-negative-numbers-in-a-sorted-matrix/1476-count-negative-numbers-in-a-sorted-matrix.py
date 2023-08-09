class Solution(object):
    def countNegatives(self, grid):
        count=0
        for i in grid:
            for j in range(len(i)):
                if i[j]<0:
                    count+=1
        return count