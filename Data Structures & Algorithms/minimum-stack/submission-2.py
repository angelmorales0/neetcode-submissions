class MinStack:

    def __init__(self):
        self.stack = []
        self.minn = [] #holds min at specific index

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.minn.append(min(self.minn[-1], val) if self.minn else val)
        return None
        

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
            self.minn.pop()
        return None
        

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        
        

    def getMin(self) -> int:
        return self.minn[-1]
