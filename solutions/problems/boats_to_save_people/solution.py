class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        
        people.sort()

        i = 0
        j = len(people) - 1

        minBoats = 0

        while i <= j:

            spaceLeft = limit - people[j]

            if people[i] <= spaceLeft:
                i += 1
                j -= 1
            else:
                j -= 1

            minBoats += 1

        return minBoats