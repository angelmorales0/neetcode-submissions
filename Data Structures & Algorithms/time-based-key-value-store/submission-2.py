class TimeMap:

    def __init__(self):
        self.timeMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        arr= []
        timestamp -= 1 #makes it the index 
        if key not in self.timeMap:
            self.timeMap[key] = []
        while timestamp >= len(self.timeMap[key]):
            self.timeMap[key].append("")
        self.timeMap[key].append(value)


        

    def get(self, key: str, timestamp: int) -> str:
        print(self.timeMap)
        ret = ""
        while timestamp >= 0:
            if key in self.timeMap and timestamp < len(self.timeMap[key]) and self.timeMap[key][timestamp] != "":
                return self.timeMap[key][timestamp]
            timestamp -= 1
        return ret
