from collections import deque

class Solution:
    def __method1 (self, image, sr, sc, color):
        if (image[sr][sc] == color): return image
        curr_color, image[sr][sc] = image[sr][sc], color
        if (((sr + 1) < len(image)) and (curr_color == image[sr + 1][sc])): self.floodFill(image, sr + 1, sc, color)
        if (((sr - 1) >= 0) and (curr_color == image[sr - 1][sc])): self.floodFill(image, sr - 1, sc, color)
        if (((sc + 1) < len(image[0])) and (curr_color == image[sr][sc + 1])): self.floodFill(image, sr, sc + 1, color)
        if (((sc - 1) >= 0) and (curr_color == image[sr][sc - 1])): self.floodFill(image, sr, sc - 1, color)
        return image

    def __method2 (self, image, sr, sc, color):
        q = deque([[sr, sc]])
        while (q):
            sr, sc = q.popleft()
            if (image[sr][sc] == color): continue
            if (((sr + 1) < len(image)) and (image[sr][sc] == image[sr + 1][sc])): q.append([sr + 1, sc])
            if (((sr - 1) >= 0) and (image[sr][sc] == image[sr - 1][sc])): q.append([sr - 1, sc])
            if (((sc + 1) < len(image[0])) and (image[sr][sc] == image[sr][sc + 1])): q.append([sr, sc + 1])
            if (((sc - 1) >= 0) and (image[sr][sc] == image[sr][sc - 1])): q.append([sr, sc - 1])
            image[sr][sc] = color
        return image

    def floodFill (self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #return self.__method1(image, sr, sc, color)
        return self.__method2(image, sr, sc, color)
