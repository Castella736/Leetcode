from typing import List;
from collections import defaultdict;
class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        # Count size of the matrix.
        m = len(mat);
        n = len(mat[0]);
        # Find candidates through row and column respectively.
        # Find the index that is the only "1" in that row/column.
        # Then return the size of intersection of sets of candidates.
        colCand = set();
        rowCand = set();
        
        # Find all row-special numbers.
        for i in range(m):
            pos = -1;
            numOne = 0;
            for j in range(n):
                if mat[i][j] == 1:
                    pos = j;
                    numOne += 1;
            if numOne == 1:
                rowCand.add((i, pos));
        
        # Find all col-special number.
        for j in range(n):
            pos = -1;
            numOne = 0;
            for i in range(m):
                if mat[i][j] == 1:
                    pos = i;
                    numOne += 1;
            if numOne == 1:
                colCand.add((pos, j));
        
        # Return the intersection.
        return len(colCand.intersection(rowCand));