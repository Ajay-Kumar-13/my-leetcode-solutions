class Solution:
    def multiply(self, num1, num2):

        if num1 == "0" or num2 == "0":
            return "0"

        n1 = list(num1)
        n2 = list(num2)
        
        l1 = len(n1)
        l2 = len(n2)
        
        product = [0]*(l1+l2)
                
        for j in range(len(n2)-1,-1,-1):
            for i in range(len(n1)-1,-1,-1):
                
                p = int(n2[j])*int(n1[i])
                
                val = p + product[i+j+1]
                
                product[i+j+1] = (val % 10)
                product[i+j] += (val // 10)
                
        start = 0
        while start < len(product) and product[start] == 0:
          start += 1                
        
        return "".join(str(i) for i in product[start:])