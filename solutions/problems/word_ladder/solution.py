from collections import deque

class Solution():
    def ladderLength(self, beginWord, endWord, wordList):

        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        wordList = list(set(wordList))
        
        wordDict = {}
        
        for word in wordList:
            for i in range(len(word)):
                w = word[:i]+"*"+word[i+1:]
                wordDict.setdefault(w, []).append(word)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])

        while len(q) > 0:
            word, ind = q.popleft()

            if word == endWord:
                return ind

            for i in range(len(word)):
                w = word[:i]+"*"+word[i+1:]
                for n in wordDict.get(w, []):
                    if n not in visited:
                        q.append((n, ind+1))
                        visited.add(n)

        return 0