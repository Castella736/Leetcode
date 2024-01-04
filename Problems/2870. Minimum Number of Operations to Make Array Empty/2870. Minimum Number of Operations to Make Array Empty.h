# include <vector>
# include <unordered_map>
using namespace std;

class Solution {
public:
    int minOperations(vector<int>& nums) {
        unordered_map<int, int> count;
        int res = 0;
        for (int num: nums) {
            count[num]++;
        }

        for (auto pair: count) {
            int freq = pair.second;
            if (freq == 1) return -1;
            // res += (freq/3) + ((freq%3) > 0);
            res += (freq+2)/3;
        }

        return res;
    }
};