import java.util.ArrayList;
import java.util.List;
class Solution {
    private int binarySearch(List<Integer> seq, int target) {
        int l = 0, r = seq.size()-1;

        while (l <= r) {
            int m = l + (r-l)/2;
            int num = seq.get(m);
            if (num == target) return m;
            else if (num < target) l = m + 1;
            else if (num > target) r = m - 1;
        }

        return l;
    }

    public int lengthOfLIS(int[] nums) {
        ArrayList<Integer> subseq = new ArrayList<>();
        for (int num: nums) {
            int pos = binarySearch(subseq, num);
            if (pos == subseq.size()) subseq.add(num);
            else subseq.set(pos, num);
        }

        return subseq.size();
    }
}