class Solution:
    def fourSum (self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        i, ans = 0, []
        while (i < (len(nums) - 3)):
            j = i + 1
            while (j < (len(nums) - 2)):
                k, l = j + 1, len(nums) - 1
                new_target = target - nums[j] - nums[i]
                while (k < l):
                    curr_sum = nums[k] + nums[l]
                    if (curr_sum > new_target): l -= 1
                    elif (curr_sum < new_target): k += 1
                    else:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        while (((k + 1) < l) and (nums[k] == nums[k + 1])): k += 1
                        while (((l - 1) > k) and (nums[l] == nums[l - 1])): l -= 1
                        k += 1 ; l -= 1
                while (((j + 1) < (len(nums) - 2)) and (nums[j] == nums[j + 1])): j += 1
                j += 1
            while (((i + 1) < (len(nums) - 3)) and (nums[i] == nums[i + 1])): i += 1
            i += 1
        return ans
