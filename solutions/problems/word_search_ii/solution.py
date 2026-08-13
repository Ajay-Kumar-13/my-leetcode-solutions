class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
        
    def put(self, key):
        self.links[ord(key)-ord('a')] = Node()
    
    def get(self, key):
        return self.links[ord(key)-ord('a')]
        
    def end(self):
        self.flag = True
    
class Solution:
        
    def __init__(self):
        self.root = Node()
        self.visited = set()
        self.board = []
        self.rows = 0
        self.cols = 0
        self.ans = set()
    
    def addWordToTrie(self, word: str) -> None:
        temp = self.root
        for x in word:
            if temp.get(x) is None:
                temp.put(x)
            temp = temp.get(x)
        temp.end()
        
    def check(self, node, i, j, word):
        if node.flag:
            self.ans.add(''.join(word))
        
        if (i, j) in self.visited:
            return False
            
        if i < 0 or i >= self.rows or j < 0 or j >= self.cols:
            return False
            
        trie = node.get(self.board[i][j])
        if trie is not None:
            self.visited.add((i, j))
            node = trie
            word.append(self.board[i][j])
            matched = self.check(node, i+1, j, word) or self.check(node, i, j+1, word) or self.check(node, i-1, j, word) or self.check(node, i, j-1, word)
            if not matched:
                word.pop()
                self.visited.remove((i, j))
                return False
            return word
        else:
            return False
        
    def findWords(self, board, words):
        self.board = board
        for word in words:
            self.addWordToTrie(word)
            
        self.rows = len(board)
        self.cols = len(board[0])
        temp = self.root
        
        for i in range(self.rows):
            for j in range(self.cols):
                if temp.get(board[i][j]) is not None:
                    self.check(temp, i, j, [])
                    self.visited.clear()
                                       
        return list(self.ans)