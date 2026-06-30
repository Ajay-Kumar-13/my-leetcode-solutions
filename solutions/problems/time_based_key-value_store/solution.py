class TimeMap(object):

    def __init__(self):
        self.HashMapV2 = {}

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if not self.HashMapV2.get(key):
            self.HashMapV2[key] = [(timestamp, value)]
        else:
            self.HashMapV2.get(key).append((timestamp, value))
        

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        values = self.HashMapV2.get(key)

        if not values:
            return ""
        
        i = 0
        j = len(values)-1
        
        while i <= j:
            mid = (i+j) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            
            if values[mid][0] > timestamp:
                j = mid - 1
            else:
                i = mid + 1
        
        if j < 0:
            return ""
            
        return values[j][1]      
