class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = []
        count = [[]for i in range(len(nums)+1)]
        mapp = {}

        for num in nums:
            mapp[num] = mapp.get(num,0) +1


        for key, value in mapp.items():
            count[value].append(key)
        for i in range(len(count)-1,-1,-1):
            if count[i] != []:
                for num in count[i]:
                    ret.append(num)
                    k-=1
                    if k == 0:
                        return ret
          
       
        
       

        return ret
        #bucket sort baby!
        
        #make an array maxing out @ 1k index

        #go thru array adding it 

        #reutrn array containing the top k lmnts 