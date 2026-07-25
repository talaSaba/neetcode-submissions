class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_beginnig,col_begginig=0,0
        row_ending,col_ending=len(matrix)-1,len(matrix[0])-1
        left=0
        right=row_ending*(len(matrix[0]))+col_ending
        while left<=right:
            middle=int((left+right)/2)
            #de sypher
            row_middle=int(middle/len(matrix[0]))
            col_middle=int(middle%len(matrix[0]))
            #now we check the binary search itself 
            if matrix[row_middle][col_middle]==target:
                return True
            elif matrix[row_middle][col_middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        
        return False

