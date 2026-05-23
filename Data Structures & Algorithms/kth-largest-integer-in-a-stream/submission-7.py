class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        # MinHeap only has 1 rule, every child must be greater than its parent
        while len(self.minHeap) > k: #pops all the smallest values until we start at the k, smallest
            heapq.heappop(self.minHeap)
    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: #heap is stored as an array, just easier to visuallize with the tree
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
            
        
