# include <vector>
# include <algorithm>
using namespace std;
class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        // Exclude empty vector.
        if (nums.empty()) return 0;

        // Sort the vector.
        sort(nums.begin(), nums.end());

        int max_streak = 0; // Record the max num of consecutive nums.
        int cur_streak = 1; // Record the num of current consecutive nums.

        for (int i=0; i < nums.size()-1; i++) {
            // Increase the count if the next number is a consecutive number.
            if (nums[i]+1 == nums[i+1]) cur_streak++;
            // Skip if the next number is the same as the current number.
            else if (nums[i] == nums[i+1]) continue; 
            // Conclude the current streak and start a new one,
            // if the next number is not consecutive to the current number.
            else {
                max_streak = std::max(max_streak, cur_streak);
                cur_streak = 1;
            }
        }
        // Conclude the last streak.
        max_streak = std::max(max_streak, cur_streak);

        return max_streak;
    }
};