from collections import deque

class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        graph = {}
        wordList.append(beginWord)
        wordList = set(wordList)
        def buildGraph(wordList):
            for word in wordList:
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    graph.setdefault(pattern, set([])).add(word)

        buildGraph(wordList)

        q = deque([(beginWord, 1)])
        visited = set([beginWord])
        
        while len(q) > 0:
            current, count = q.popleft()

            for i in range(len(current)):
                pattern = current[:i]+'*'+current[i+1:]
                children = graph.get(pattern)
                
                for child in children:
                    if child == endWord:
                        return count+1
                    if child not in visited:
                        q.append((child, count+1))
                        visited.add(child)

        return 0

            

