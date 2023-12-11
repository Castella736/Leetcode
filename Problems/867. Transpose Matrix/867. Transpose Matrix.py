class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        # Suppose this is a m by n matrix.
        m = len(matrix);
        n = len(matrix[0]);
        T = [[0 for _ in range(m)] for _ in range(n)];
        # In python we cannot initialize T as
        # [[0]*m]*n
        # Since the inner [0] will point to the same array.
        
        
        for i in range(m):
            for j in range(n):
                T[j][i] = matrix[i][j];
                
        return T;