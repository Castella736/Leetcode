class Solution {
    private int countOne(String s) {
        int res = 0; 
        for (char ch: s.toCharArray()) {
            res += ch-'0';
        }
        return res;
    }
    
    public int numberOfBeams(String[] bank) {
        int res = 0;
        int cur_count, prev_count = 0;
        
        for (String row : bank) {
            cur_count = countOne(row);
            if (cur_count > 0) {
                res += cur_count * prev_count;
                prev_count = cur_count;
            }
        }

        return res;
    }
}