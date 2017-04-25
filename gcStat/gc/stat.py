class stats():
    minHeapVal = -1
    maxheapVal = -1

    def __init__(self, min ,max):
        self.minHeapVal = min
        self.maxheapVal = max

    def getMin(self):
        return self.minHeapVal

    def getmax(self):
        return self.maxheapVal
