# include <vector>
using namespace std;
class Solution {
public:
    int findSpecialInteger(vector<int>& arr) {
        // Exclude singleton list.
        if (arr.size() == 1) return arr[0];

        // Set counter.
        int COUNT = arr.size() / 4;
        int cur_streak = 1;

        // Count the maximum streak.
        for (int i = 1; i < arr.size(); i++){
            if (arr[i] == arr[i-1]) {
                cur_streak += 1;
                if (cur_streak > COUNT) return arr[i];
            }
            else {
                cur_streak = 1;
            }
        }

        return -1;
    }
};