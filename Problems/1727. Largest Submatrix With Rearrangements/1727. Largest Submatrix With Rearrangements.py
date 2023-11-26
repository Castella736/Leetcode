class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        # Calculate size of the matrix.
        n = len(matrix);
        m = len(matrix[0]);
        
        # Use prefix sum to record how many consecutive 1 are above the position
        # in the same column.
        for i in range(1,n):
            for j in range(m):
                matrix[i][j] += matrix[i-1][j] if matrix[i][j]!=0 else 0;
        
        # Sort over rows and find result with greedy algorithm.
        res = 0;
        for row in matrix:
            row.sort(reverse=True);
            for n_col, height in enumerate(row, 1):
                res = max(res, n_col*height);
        
        return res;