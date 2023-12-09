import java.util.Arrays;
import java.lang.Math;
class Solution {
    public int longestConsecutive(int[] nums) {
        // Exclude empty list.
        if (nums.length == 0) return 0;
        
        Arrays.sort(nums); // Sort the array.
        int max_streak = 0; // Record the max num of consecutive nums.
        int cur_streak = 1; // Record the num of current consecutive nums.

        for (int i=0; i < nums.length-1; i++) {
            // Increase the count if the next number is a consecutive number.
            if (nums[i]+1 == nums[i+1]) cur_streak++;
            // Skip if the next number is the same as the current number.
            else if (nums[i] == nums[i+1]) continue; 
            // Conclude the current streak and start a new one,
            // if the next number is not consecutive to the current number.
            else {
                max_streak = Math.max(max_streak, cur_streak);
                cur_streak = 1;
            }
        }
        // Conclude the last streak.
        max_streak = Math.max(max_streak, cur_streak);

        // Return the result.
        return max_streak;
    }
}