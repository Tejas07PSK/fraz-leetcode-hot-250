from math import atan2, pi

class Solution:
    def visiblePoints (self, points: List[List[int]], angle: int, location: List[int]) -> int:
        x_start, y_start = location
        same_points, new_list = 0, []
        for i in range(len(points)):
            x_end, y_end = points[i]
            if ((x_end == x_start) and (y_end == y_start)):
                same_points += 1
                continue
            new_list.append(atan2(y_end - y_start, x_end - x_start))
        angle *= pi / 180.0
        new_list.sort() ; n = len(new_list)
        for i in range(n): new_list.append(new_list[i] + 2.0 * pi)
        start, ans = 0, 0
        for end in range(len(new_list)):
            while ((new_list[end] - new_list[start]) > angle): start += 1
            ans = max(ans, end - start + 1)
        return ans + same_points
