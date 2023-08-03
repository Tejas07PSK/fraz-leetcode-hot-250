class Solution:
    def canCompleteCircuit (self, gas: List[int], cost: List[int]) -> int:
        start, tot_fuel_left, curr_fuel_left = 0, 0, 0
        for i in range(len(gas)):
            tot_fuel_left += gas[i] - cost[i]
            curr_fuel_left += gas[i] - cost[i]
            if (curr_fuel_left < 0):
                curr_fuel_left, start = 0, i + 1
        return start if (tot_fuel_left >= 0) else -1
