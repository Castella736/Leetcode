import java.util.ArrayList;
import java.util.List;
class Solution {
    public int numSpecial(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int res = 0; // record the result.
        List<Integer> colCand = new ArrayList<>();

        // Find all column candidate.
        for (int[] row: mat) {
            int nOne = 0;
            int pos = 0;
            for (int j = 0; j < n; j++) {
                if (row[j] == 1) {
                    nOne += 1;
                    pos = j; 
                }
            }
            if (nOne == 1) colCand.add(pos);
        }

        // Verify candidate columns.
        for (int col: colCand) {
            int nOne = 0;
            for (int i = 0; i < m; i++)
                nOne += mat[i][col];
            if (nOne == 1) res += 1;
        }

        return res;
    }
}