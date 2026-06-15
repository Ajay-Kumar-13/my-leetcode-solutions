class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # validate rows and coloums
        
        for i in range(9):
            row = set()
            col = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                if board[i][j] in col:
                    return False
                col.add(board[i][j])

            for j in range(9):
                if board[j][i] == ".":
                    continue
                if board[j][i] in row:
                    return False
                row.add(board[j][i])
        # check subboxes
        subgrids = [(0,3), (0,6), (0,9), (3, 3), (3, 6), (3, 9), (6, 3), (6, 6), (6, 9)]

        for i, j in subgrids:
            box = set()
            for k in range(i, i+3):
                for l in range(j-3, j):
                    if board[k][l] == ".":
                        continue
                    if board[k][l] in box:
                        return False
                    box.add(board[k][l])

        return True