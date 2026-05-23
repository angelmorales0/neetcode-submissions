class MedianFinder:

    def __init__(self):
        self.median = 0
        self.length = 0
        self.middle = -1
        self.stream=[]
        

    def addNum(self, num: int) -> None:
        self.stream.append(num)
        self.stream.sort()

        if self.length % 2 == 0: #even case
            self.middle +=1 
            self.median = self.stream[self.middle]
            self.length +=1
        else:
            self.median =  (self.stream[self.middle] +  self.stream[self.middle + 1]) / 2
            self.length +=1

        

    def findMedian(self) -> float:
        return self.median

#Only need to worry about the middle value 
#-> [1] -> 1 [1,2] = middle index (0) + next index(1) / 2) for if it is odd len
#if it is even length then shift index up by 1 
#prev middle index shifts up 1 
#[1][2][3] [4][5]
      
        