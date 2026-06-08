class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        str = ""
        stack = []

        for char in list(s.lower()):
            if char.isalnum():
                str += char

        for i in range(len(str) // 2):
            stack.append(str[i])

        if (len(str)%2 == 0):
            for i in range((len(str)//2), len(str)):
                if stack.pop() != str[i]:
                    return False
        else:
            for i in range((len(str)//2)+1, len(str)):
                if stack.pop() != str[i]:
                    return False

        return True