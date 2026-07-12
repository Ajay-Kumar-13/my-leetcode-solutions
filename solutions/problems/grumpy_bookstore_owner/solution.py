class Solution(object):
    def maxSatisfied(self, customers, grumpy, minutes):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type minutes: int
        :rtype: int
        """
        
        satisfied_customers = 0

        max_unsatisfied_customers = 0

        for i in range(minutes):
            if grumpy[i] == 0:
                satisfied_customers += customers[i]
            else:
                max_unsatisfied_customers += customers[i]

        i = 1
        j = minutes

        max_unsatisfied_customers_in_window = max_unsatisfied_customers

        while j < len(customers):
            if grumpy[i-1] == 1:
                max_unsatisfied_customers_in_window -= customers[i-1]
                
            if grumpy[j] == 1:
                max_unsatisfied_customers_in_window += customers[j]
            else:
                satisfied_customers += customers[j]
                
            max_unsatisfied_customers = max(max_unsatisfied_customers_in_window, max_unsatisfied_customers)
            
            i += 1
            j += 1
        
        return satisfied_customers+max_unsatisfied_customers