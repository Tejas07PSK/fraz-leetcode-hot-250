class Solution:
    def getPermutation (self, n: int, k: int) -> str:
        facts, nums = [1 for i in range(n)], [str(i) for i in range(1, n + 1)]
        for i in range(1, n): facts[i] = i * facts[i - 1]
        res = [] ; k -= 1
        while (len(nums) > 0):
            idx = k // facts[len(nums) - 1]
            res.append(nums[idx])
            k %= facts[len(nums) - 1]
            nums.pop(idx)
        return "".join(res)
