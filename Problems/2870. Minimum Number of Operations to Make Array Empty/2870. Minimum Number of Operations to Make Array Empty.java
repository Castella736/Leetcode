import java.util.HashMap;
class Solution {
    public int minOperations(int[] nums) {
        Arrays.sort(nums);
        int res = 0;
        int count = 1;

        for (int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1]) count++;
            else {
                if (count == 1) return -1;
                res += (count+2) / 3;
                count = 1;
            }
        }
        if (count == 1) return -1;
        res += (count+2) / 3;

        return res;
    }
}