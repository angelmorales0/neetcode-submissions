class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s = []
        e = []
        ret = []
        curr = []
        intervals.sort(key=lambda pair: pair[0])

        for start, end in intervals:
            s.append(start)
            e.append(end)   
        print(s,e)
        length = 0
        for i in range(len(s)+1):    
            if i >= len(s) or e[0] < s[i]:
                maxE = max(e[:i])
                if i < len(s) and maxE >= s[i]:
                    continue

                ret.append([min(curr), maxE]) # must clear dupes later 
                curr.clear()
                #must get length to find max E
                #interval ends 
            if i< len(s):
                curr.append(s[i])
    

        return ret

        