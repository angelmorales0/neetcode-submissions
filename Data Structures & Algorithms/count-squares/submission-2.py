class CountSquares:

    def __init__(self):
        self.points = {}
        

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)]= self.points.get(tuple(point),0) + 1
        

    def count(self, point: List[int]) -> int:
        points = self.points
        size = 1
        count = 0
        x, y = point

        for size in range(1,1001):
            pCount = count # I THINK THIS DOES JUST THE REFERENCE NOT A COPY..

            #checkleft UP
            count +=  points.get((x-size,y), 0) * points.get((x,y+size), 0) *  points.get((x-size,y+size),0)
            #checkleft DOWN
            count +=  points.get((x-size,y), 0) * points.get((x,y-size), 0) *  points.get((x-size,y-size),0)


            #check right UP
            count +=  points.get((x+size,y), 0) * points.get((x,y+size), 0) *  points.get((x+size,y+size),0)


            #check right DOWN
            count +=  points.get((x+size,y), 0) * points.get((x,y-size), 0) *  points.get((x+size,y-size),0)
        return count

        
        
    '''
    m 
        x -s, 

    for dist 1. combo is 

        Left, up/down x-1, y+1 |  x -1 , y -1 
        
        Right up / down| x+1, y-1 |  x+ 1, y+ 1 |

        and from there diag is the sum of btoh 
        Now need to check till we reach bounds 
        THE DIAGNOL IS ALWAYS A MATCH AND THESE ARE THE ONLY 4 direcions it can go 

    '''
