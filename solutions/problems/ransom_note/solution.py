class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        ransomNote = list(ransomNote)
        magazine = list(magazine)

        ransomNote.sort()
        magazine.sort()

        i = 0
        j = 0
        count = 0

        if len(ransomNote) > len(magazine):
            return False

        while j < len(magazine) - 1:
            if ransomNote[i] == magazine[j]:
                count += 1
                i += 1
            
            if j < len(magazine) - 1:
                j += 1

            if count == len(ransomNote):
                return True
                
        if ransomNote[i] == magazine[j]:
                count += 1

        if count == len(ransomNote):
            return True
        else:
            return False
        