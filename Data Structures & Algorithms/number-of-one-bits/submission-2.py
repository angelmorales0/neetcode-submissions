class Solution:
    def hammingWeight(self, n: int) -> int:
     
        vals = [0,1]

        while vals[-1] <= (math.ceil(n/2)):
            vals.append((vals[-1])*2)

        count = 0
        print(vals)

        for value in vals[::-1]:
            print(value,n, count)
            if value <= n:
                n -= value
                count +=1
            if n <= 0:
                return count
        return count
        
        """
        Is it greedy?
        Yes we alwayst ake the next highrst bit thats how it wroks 
        """
        