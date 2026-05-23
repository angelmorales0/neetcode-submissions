class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        heapq.heapify(nums)
        #creates our heap
        while len(nums) > k :
              heapq.heappop(nums)#pops the smallest lmnt  making our heap be the k biggest elemnts and heap[0] the kth largest lmt 

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
