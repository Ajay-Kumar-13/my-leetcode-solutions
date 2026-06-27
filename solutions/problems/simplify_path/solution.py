class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        path = path.split("/")
        
        sp = []
        
        for ele in path:
            if ele == "":
                continue
            
            if ele == ".":
                continue
                
            if ele == "..":
                if len(sp) > 0:
                    sp.pop()
                continue
                
            if len(sp) <= 0:
                sp.append(ele)
                continue

            # if sp[-1] == ele:
            #     continue 

            sp.append(ele)
            
        return "/" + "/".join(sp)