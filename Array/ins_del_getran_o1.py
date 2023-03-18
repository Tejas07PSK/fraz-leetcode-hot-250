from random import randint
class RandomizedSet:
    def __init__ (self):
        self.hm, self.lst = {}, []
        self.sz = 0

    def insert (self, val: int) -> bool:
        if (val in self.hm): return False
        if (self.sz == len(self.lst)): self.lst.append(val)
        else: self.lst[self.sz] = val
        self.hm[val] = self.sz
        self.sz += 1
        return True

    def remove (self, val: int) -> bool:
        if (val not in self.hm): return False
        self.lst[self.hm[val]] = self.lst[self.sz - 1]
        self.hm[self.lst[self.sz - 1]] = self.hm[val]
        self.lst[self.sz - 1] = None ; del self.hm[val]
        self.sz -= 1
        return True

    def getRandom (self) -> int: return self.lst[randint(0, self.sz - 1)]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
