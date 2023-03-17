class Solution:
    def productExceptSelf (self, nums: List[int]) -> List[int]:
        product_arr = [1 for i in range(len(nums))]
        for i in range(1, len(nums)): product_arr[i] = nums[i - 1] * product_arr[i - 1]
        prd_rt = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            product_arr[i] *= prd_rt
            prd_rt *= nums[i]
        return product_arr
