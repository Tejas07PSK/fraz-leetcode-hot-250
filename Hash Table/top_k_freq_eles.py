from random import randint

class Solution:
    def __quickPartition (self, arr, left, right):
        pvt_idx = randint(left, right)
        pvt = arr[pvt_idx][0]
        arr[pvt_idx], arr[right] = arr[right], arr[pvt_idx]
        i, j = left, left
        while (i <= right):
            if (arr[i][0] >= pvt):
                arr[j], arr[i] = arr[i], arr[j]
                j += 1
            i += 1
        return j - 1

    def __quickSelect (self, arr, left, right, k):
        if (left >= right): return
        quick_idx = self.__quickPartition(arr, left, right)
        if ((quick_idx + 1) == k): return
        elif ((quick_idx + 1) > k): self.__quickSelect(arr, left, quick_idx - 1, k)
        else: self.__quickSelect(arr, quick_idx + 1, right, k)

    def topKFrequent (self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            if (num not in hm): hm[num] = 1
            else: hm[num] += 1
        arr = [(value, key) for key, value in hm.items()]
        self.__quickSelect(arr, 0, len(arr) - 1, k)
        #print(arr)
        return [arr[i][1] for i in range(k)]
