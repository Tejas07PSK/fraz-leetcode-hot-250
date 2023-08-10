class Solution:
    def candy (self, ratings: List[int]) -> int:
        ans, i = 0, 0
        while (i < len(ratings)):
            while (((i + 1) < len(ratings)) and (ratings[i] == ratings[i + 1])):
                ans += 1
                i += 1
            if (i == (len(ratings) - 1)):
                ans += 1 ; i += 1
                continue
            up_peak = 0
            while (((i + 1) < len(ratings)) and (ratings[i] < ratings[i + 1])):
                up_peak += 1
                ans += up_peak
                i += 1
            ans += up_peak + 1
            if ((i == (len(ratings) - 1)) or (((i + 1) < len(ratings)) and (ratings[i] == ratings[i + 1]))):
                i += 1
                continue
            down_peak = 0
            while (((i + 1) < len(ratings)) and (ratings[i] > ratings[i + 1])):
                down_peak += 1
                ans += down_peak
                i += 1
            ans += down_peak + 1
            ans -= min(up_peak + 1, down_peak + 1)
            if ((i == (len(ratings) - 1)) or (((i + 1) < len(ratings)) and (ratings[i] == ratings[i + 1]))):
                i += 1
            elif (((i + 1) < len(ratings)) and (ratings[i] < ratings[i + 1])):
                ans -= 1
        return ans
