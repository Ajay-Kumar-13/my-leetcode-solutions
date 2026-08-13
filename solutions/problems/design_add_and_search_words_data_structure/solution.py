class Node:
    def __init__(self):
        self.links = [None]*26
        self.flag = False
        
    def containsKey(self, key):
        return self.links[ord(key)-ord('a')]
        
    def put(self, key):
        self.links[ord(key)-ord('a')] = Node()
    
    def get(self, key):
        return self.links[ord(key)-ord('a')]
        
    def end(self):
        self.flag = True

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        temp = self.root
        for x in word:
            if temp.containsKey(x) is None:
                temp.put(x)
            temp = temp.get(x)
        temp.end()
        
    def dfs(self, node, ind, word):
        
        temp = node
        
        if ind == len(word):
            return temp.flag
        
        if word[ind] == ".":
            for trie in temp.links:
                if trie is not None:
                    if self.dfs(trie, ind+1, word):
                        return True
            return False
        else:
            if temp.containsKey(word[ind]) is None:
                return False
            
            return self.dfs(temp.get(word[ind]), ind+1, word)
        

    def search(self, word: str) -> bool:
        
        temp = self.root
        for ind, x in enumerate(word):
            if x == ".":
                return self.dfs(temp, ind, word)
            else:
                if temp.containsKey(x) is None:
                    return False
            
            temp = temp.get(x)
            
        return temp.flag