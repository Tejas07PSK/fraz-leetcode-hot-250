class Solution:
    def nextGreaterElement (self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater, stk = [-1 for i in range(len(nums2))], []
        for i in range(len(nums2)):
            while ((stk) and (nums2[stk[-1]] < nums2[i])): next_greater[stk.pop()] = nums2[i]
            stk.append(i)
        stk.clear()
        num2_idx_map = {num : idx for idx, num in enumerate(nums2)}
        return [next_greater[num2_idx_map[num]] for num in nums1]
