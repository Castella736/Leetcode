class Solution {
    public int maxScore(String s) {
        int l_comp = (s.charAt(0) == '0') ? 1 : 0;
        int best_l_comp = l_comp;
        int n_ones = 0;
        for (int i = 1; i < s.length()-1; i++) {
            if (s.charAt(i) == '0') l_comp++;
            else {
                l_comp--;
                n_ones++;
            }

            if (l_comp > best_l_comp) best_l_comp = l_comp;
        }
        n_ones += (s.charAt(s.length()-1) == '1') ? 1 : 0;

        return best_l_comp + n_ones;
    }
}