# include <algorithm>
class Solution {
public:
    int maxProduct(vector<int>& nums) {
        int maxVal = -1;
        int sMaxVal = -1;

        for (auto num: nums) {
            if (num > maxVal) std::swap(num, maxVal);
            sMaxVal = std::max(num, sMaxVal);
        }

        return (sMaxVal - 1) * (maxVal - 1);
    }
};