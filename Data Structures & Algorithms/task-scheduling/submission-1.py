class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = []
        for key in count:
            maxHeap.append(-count[key])
        heapq.heapify(maxHeap)

        q = deque()
        time = 0 
        while maxHeap or q:
            time += 1
            if maxHeap: 
                newCount = 1 + heapq.heappop(maxHeap)
                if newCount !=0 :
                    q.append([newCount, time+n])
            if q and q[0][1] == time:
                #cd is over
                cd = q.popleft()
                heapq.heappush(maxHeap, cd[0])
        return time
        