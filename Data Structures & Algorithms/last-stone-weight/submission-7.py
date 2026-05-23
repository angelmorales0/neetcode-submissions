class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        rev = []
        for s in stones:
            rev.append(-s)
        heapq.heapify(rev) #makes it a max heap w/ most neg being at top
        #rev is now a heap
        while len(rev) > 1:
            print(rev)

            first = rev[0]
            if len(rev) >= 3:

                if rev[1] < rev[2]:
                    second = rev[1]
                else:
                    second = rev[2]
            else:
                second = rev[1]
            
            print(second,"2")
            print(first)

            if first < second:
                readd = first - second  #stone weight is shifted down
                print(readd,"re")
                heapq.heappop(rev) # so stone to be deleted is at top
                heapq.heappop(rev)
                heapq.heappush(rev,readd)
                
            elif second < first:
                readd = second - first  #stone weight is shifted down 
                heapq.heappop(rev) # so stone to be deleted is at top
                heapq.heappop(rev)
                heapq.heappush(rev,readd)
            else: 
                heapq.heappop(rev)
                heapq.heappop(rev)
        if rev:
            return -rev[0]
        return 0
        