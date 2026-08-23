class Solution:
    def getIntersectionNode(self, headA, headB):
        
        a = headA
        b = headB

        LifeA, LifeB = True, True

        while a and b:

            if a == b:
                return a

            a = a.next            
            if a is None and LifeA:
                a = headB
                LifeA = False
            
            b = b.next
            if b is None and LifeB:
                b = headA
                LifeB = False

        return None