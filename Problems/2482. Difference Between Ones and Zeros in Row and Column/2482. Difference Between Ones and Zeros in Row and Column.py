from itertools import product;
class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0]);
        onesRow = [row.count(1) for row in grid];
        onesCol = [col.count(1) for col in zip(*grid)];

        for i, j in product(range(m), range(n)):
            grid[i][j] = (2*onesRow[i]-n) + (2*onesCol[j]-m);

        return grid;