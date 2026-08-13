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

class Trie:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        temp = self.root
        for x in word:
            if temp.containsKey(x) is None:
                temp.put(x)    
            temp = temp.get(x)
        temp.end()

    def search(self, word: str) -> bool:
        temp = self.root
        for x in word:
            if temp.get(x) is None:
                return False
            temp = temp.get(x)
            
        return temp.flag

    def startsWith(self, prefix: str) -> bool:
        
        temp = self.root
        for x in prefix:
            if temp.get(x) is None:
                return False
            temp = temp.get(x)
        
        return True