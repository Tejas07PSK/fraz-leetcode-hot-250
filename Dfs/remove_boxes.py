from functools import lru_cache

class Solution:

    @lru_cache(None)
    def __helper (self, left, right, count_of_same_as_left):
        if (left > right): return 0
        while (((left + 1) <= right) and (self.boxes[left] == self.boxes[left + 1])):
            left += 1
            count_of_same_as_left += 1
        ans = ((count_of_same_as_left + 1) * (count_of_same_as_left + 1)) + self.__helper(left + 1, right, 0)
        for k in range(left + 1, right + 1):
            if (self.boxes[k] == self.boxes[left]):
                ans = max(ans, self.__helper(left + 1, k - 1, 0) + self.__helper(k, right, count_of_same_as_left + 1))
        return ans

    def removeBoxes (self, boxes):
        self.boxes = boxes
        return self.__helper(0, len(boxes) - 1, 0)
