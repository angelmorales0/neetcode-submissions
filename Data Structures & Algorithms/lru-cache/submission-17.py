class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        

    def get(self, key: int) -> int:
        if key in self.cache:
            re_add = self.cache.pop(key)
            self.cache[key] = re_add
            return self.cache[key]

        return -1

        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:

            if self.cap == 0:
                keys = list(self.cache.keys())[0]
                self.cache.pop(keys) #first key
                self.cache[key] = value
            else:
                self.cache[key] = value
                self.cap -= 1
        else:
            self.cache.pop(key)
            self.cache[key]= value
        
