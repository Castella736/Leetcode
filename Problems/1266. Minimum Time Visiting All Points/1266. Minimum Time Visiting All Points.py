class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        res = 0;
        for i, point in enumerate(points[1:], 1):
            res += max(
                abs(point[0] - points[i-1][0]),
                abs(point[1] - points[i-1][1]),
            );
            
        return res;