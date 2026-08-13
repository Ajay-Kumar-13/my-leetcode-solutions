class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        rows = len(board)
        cols = len(board[0])
        
        visited = set([])
        
        def check(i, j, ind):

            if ind == len(word):
                return True
            
            if (i, j) in visited:
                return False
                
            if i < 0 or i >= rows or j < 0 or j >= cols:
                return False
            
            if board[i][j] == word[ind]:
                visited.add((i, j))
                ind += 1
            else:
                return False
            
            if (check(i+1, j, ind) or check(i, j+1, ind) or check(i-1, j, ind) or check(i, j-1, ind)) is False:
                visited.remove((i, j))
                return False
                
            return True
        
        for i in range(rows):
            for j in range(cols):
                    
                if board[i][j] == word[0]:

                    found = check(i, j, 0)
                    
                    if found is True:
                        return True
            
        check(0, 0, 0)
        return False