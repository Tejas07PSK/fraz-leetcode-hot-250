class Solution:
    def sortedSquares (self, nums: List[int]) -> List[int]:
        i, arr = 0, [0 for i in range(len(nums))]
        while ((i < len(nums)) and (nums[i] < 0)): i += 1
        j, i, k = i, i - 1, 0
        while (i >= 0) and (j < len(nums)):
            if (-nums[i] <= nums[j]):
                arr[k] = nums[i] * nums[i]
                i -= 1
            else:
                arr[k] = nums[j] * nums[j]
                j += 1
            k += 1
        while (i >= 0):
            arr[k] = nums[i] * nums[i]
            i -= 1 ; k += 1
        while (j < len(nums)):
            arr[k] = nums[j] * nums[j]
            j += 1 ; k += 1
        return arr
