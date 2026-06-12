class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """

        if len(chars) < 2:
            return 1
        
        i = 0 
        j = i + 1
        k = 0

        count = 1

        s = ""

        while i < j and i < len(chars) - 1:
            if chars[i] == chars[j]:
                count += 1
            else:
                s += chars[i]
                if count > 1:
                    s += str(count)
                count = 1
                k = j

            i += 1
            j = i + 1

        s += chars[j-1]
        if count > 1:
            s += str(count)

        s = list(s)

        for i in range(len(chars)):
            if i > len(s)-1:
                break
            chars[i] = s[i]

        return len(s)