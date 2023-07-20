class Solution:
    def __method1 (self, nums):
        max_num1, max_num2, max_num3 = -inf, -inf, -inf
        min_num1, min_num2 = inf, inf
        for num in nums:
            if (num > max_num1):
                max_num3 = max_num2
                max_num2 = max_num1
                max_num1 = num
            elif (num > max_num2):
                max_num3 = max_num2
                max_num2 = num
            elif (num > max_num3): max_num3 = num
            if (num < min_num1):
                min_num2 = min_num1
                min_num1 = num
            elif (num < min_num2): min_num2 = num
        return max((min_num1 * min_num2 * max_num1), (max_num1 * max_num2 * max_num3))

    def __method2 (self, nums):
        nums.sort() ; return max((nums[-1] * nums[-2] * nums[-3]), (nums[0] * nums[1] * nums[-1]))

    def maximumProduct (self, nums: List[int]) -> int:
        #return self.__method1(nums)
        return self.__method2(nums)
