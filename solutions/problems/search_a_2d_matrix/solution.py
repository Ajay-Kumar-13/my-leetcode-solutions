class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        n = (len(matrix) * len(matrix[0]))-1

        i = 0
        j = n

        while i <= j:
            mid = (i+j) // 2

            row = mid // len(matrix[0])
            col = mid % len(matrix[0])

            if matrix[row][col] == target:
                return True

            if matrix[row][col] > target:
                j = mid - 1
            else:
                i = mid + 1

        return False

            
