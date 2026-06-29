class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        i = 0
        m = len(matrix)
        n = len(matrix[0])
        j = m * n - 1

        while i <= j:
            mid = (i + j) // 2

            row = mid // n
            col = mid % n

            if target == matrix[row][col]:
                return True
            elif target > matrix[row][col]:
                i = mid + 1
            else:
                j = mid - 1
                        
        return False