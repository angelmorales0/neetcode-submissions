class Solution:
    def countBits(self, n: int) -> List[int]:

        def count(num):
            ret = 0
            while num > 0:
                ret += num %2 
                num = num >>1
            return ret
        
        ret = []
        for i in range(n+1):
            ret.append(count(i))
        return ret
      