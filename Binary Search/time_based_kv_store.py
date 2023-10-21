from bisect import bisect_right

class TimeMap:
    def __init__ (self): self.hm = {}

    def set (self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.hm): self.hm[key] = []
        self.hm[key].append((value, timestamp))

    def get (self, key: str, timestamp: int) -> str:
        if (key not in self.hm): return ""
        lst = self.hm[key]
        idx = bisect_right(lst, timestamp, key=lambda x: x[1])
        if (idx == 0): return ""
        return lst[idx - 1][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
