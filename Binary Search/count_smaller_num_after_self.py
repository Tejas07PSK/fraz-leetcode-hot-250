from bisect import bisect_left
from array import array

class Solution:
    def __method1 (self, nums):
        self.new_nums = [(nums[i], i) for i in range(len(nums))]
        self.res = [0 for i in range(len(nums))]
        self.__mergesort(0, len(nums) - 1)
        return self.res

    def __merge (self, left, mid, right):
        ptr1, ptr2, ptr = left, mid + 1, 0
        n1, n2 = mid, right
        temp, count = [0 for i in range(right - left + 1)], 0
        while ((ptr1 <= n1) and (ptr2 <= n2)):
            if (self.new_nums[ptr1][0] <= self.new_nums[ptr2][0]):
                temp[ptr] = self.new_nums[ptr1]
                self.res[self.new_nums[ptr1][1]] += count
                ptr1 += 1
            else:
                temp[ptr] = self.new_nums[ptr2]
                count += 1 ; ptr2 += 1
            ptr += 1
        while (ptr1 <= n1):
            temp[ptr] = self.new_nums[ptr1]
            self.res[self.new_nums[ptr1][1]] += count
            ptr1 += 1 ; ptr += 1
        while (ptr2 <= n2):
            temp[ptr] = self.new_nums[ptr2]
            count += 1 ; ptr2 += 1 ; ptr += 1
        ptr = 0
        while (left <= right):
            self.new_nums[left] = temp[ptr]
            left += 1 ; ptr += 1

    def __mergesort (self, left, right):
        if (left < right):
            mid = left + ((right - left) // 2)
            self.__mergesort(left, mid)
            self.__mergesort(mid + 1, right)
            self.__merge(left, mid, right)

    def __method2 (self, nums):
        new_nums, res = array('h'), [0 for i in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            j = bisect_left(new_nums, nums[i])
            new_nums.insert(j, nums[i])
            res[i] = j
        return res

    def countSmaller (self, nums: List[int]) -> List[int]:
        #return self.__method1(nums)
        return self.__method2(nums)
