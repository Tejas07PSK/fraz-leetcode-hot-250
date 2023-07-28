class Solution:
    def __calc_dist (self, p1, p2): return (((p2[0] - p1[0]) ** 2) + ((p2[1] - p1[1]) ** 2))
    def validSquare (self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4] ; points.sort(key=lambda x : (x[0], x[1]))
        side1 = self.__calc_dist(points[0], points[1])
        if (side1 == 0): return 0
        side2 = self.__calc_dist(points[1], points[3])
        if (side2 == 0): return 0
        side3 = self.__calc_dist(points[3], points[2])
        if (side3 == 0): return 0
        side4 = self.__calc_dist(points[2], points[0])
        if (side4 == 0): return 0
        dg1, dg2 = self.__calc_dist(points[1], points[2]), self.__calc_dist(points[0], points[3])
        return (side1 == side2) and (side2 == side3) and (side3 == side4) and (side4 == side1) and (dg1 == dg2)
