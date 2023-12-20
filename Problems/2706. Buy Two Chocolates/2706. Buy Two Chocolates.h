# include <limits.h>
class Solution {
public:
    int buyChoco(vector<int>& prices, int money) {
        int min_val[] = {INT_MAX, INT_MAX};
        for (const auto& price : prices) {
            if (price < min_val[0]) {
                min_val[1] = min_val[0];
                min_val[0] = price;
            }
            else if (price < min_val[1]) min_val[1] = price;
        }

        return money-min_val[0]-min_val[1] < 0 ? money : money-min_val[0]-min_val[1];
    }
};