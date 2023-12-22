class Solution {
public:
     int maxScore(string s) {
        int l_comp = (s[0] == '0') ? 1 : 0;
        int best_l_comp = l_comp;
        int n_ones = 0;
        for (int i = 1; i < s.size()-1; i++) {
            if (s[i] == '0') l_comp++;
            else {
                l_comp--;
                n_ones++;
            }

            if (l_comp > best_l_comp) best_l_comp = l_comp;
        }
        n_ones += (s[s.size()-1] == '1') ? 1 : 0;

        return best_l_comp + n_ones;
    }
};