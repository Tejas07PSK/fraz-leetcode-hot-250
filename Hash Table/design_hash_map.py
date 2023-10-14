class MyHashMap:
    def __init__ (self):
        self.size = 19997
        self.mult = 12582917
        self.data = [[None] for _ in range(self.size)]

    def __get_hash_idx (self, key): return key * self.mult % self.size

    def put (self, key: int, value: int) -> None:
        self.remove(key)
        lst = self.data[self.__get_hash_idx(key)]
        i = 0
        while (i < len(lst)):
            if (lst[i] == None): break
            i += 1
        if (i == len(lst)): lst.append((key, value))
        else: lst[i] = (key, value)

    def get (self, key: int) -> int:
        lst = self.data[self.__get_hash_idx(key)]
        i = 0
        while (i < len(lst)):
            if (lst[i] and (lst[i][0] == key)): return lst[i][1]
            i += 1
        return -1

    def remove (self, key: int) -> None:
        lst = self.data[self.__get_hash_idx(key)]
        i = 0
        while (i < len(lst)):
            if (lst[i] and (lst[i][0] == key)):
                lst[i] = None
                break
            i += 1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
