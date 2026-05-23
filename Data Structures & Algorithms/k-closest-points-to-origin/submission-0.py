class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def distance(arr):
            x1, y1 = 0, 0
            x2 = arr[0]
            y2 = arr[1]
            return math.sqrt( ((x1-x2)**2 + (y1-y2)**2))

    #we can make a max heap to keep track of the 3 biggest elemnts
        ret = []
        heapq.heapify(ret)
        for point in points:
            heapq.heappush(ret,[-(distance(point)), point]) #pushes the neg of 
        #the current value onto the heap
            while len(ret) > k:
                heapq.heappop(ret) #pops the most negative (furhtest away)value 
            #until we have the k values we are looking for
       
        res = []
        for result in ret:
            res.append(result[1])
        return res

        