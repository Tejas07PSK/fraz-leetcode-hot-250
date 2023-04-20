from random import choice

class RandomizedCollection:
    def __init__(self):
        self.lst = [] ; self.hm = {}

    def insert(self, val: int) -> bool:
        self.lst.append(val)
        if (val in self.hm):
            self.hm[val].add(len(self.lst) - 1)
            return False
        self.hm[val] = {len(self.lst) - 1}
        return True

    def remove (self, val: int) -> bool:
        if (val not in self.hm): return False
        last_char = self.lst.pop()
        self.hm[last_char].discard(len(self.lst))
        if (self.lst and self.hm[val]):
            idx = self.hm[val].pop()
            self.hm[last_char].add(idx)
            self.lst[idx] = last_char
        if (not self.hm[val]): del self.hm[val]
        return True

    def getRandom (self) -> int: return choice(self.lst)

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
