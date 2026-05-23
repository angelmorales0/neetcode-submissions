class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums
        self.nums.sort()
        print(self.nums)
      
        

    def add(self, val: int) -> int:
        num_added = False
        for i in range(len(self.nums)):
            if i!= 0 and self.nums[i] > val:#we insert at spot before 
                self.nums.insert(i,val)
                num_added = True
                break
            elif i == 0 and self.nums[i] > val:
                self.nums.insert(0,val)
                num_added = True
                break
        if not num_added:
            self.nums.append(val)
        index = len(self.nums) - self.k
        return self.nums[index]

            
        
