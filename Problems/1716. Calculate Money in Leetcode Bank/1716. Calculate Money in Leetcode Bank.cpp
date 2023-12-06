class Solution {
public:
    int totalMoney(int n) {
        int w = n / 7; // Passed weeks.
        short l = n % 7; // Remain days.
        int res = 21*w + 7*(w*(w+1))/2;

        res += l*w + l*(l+1)/2;

        return res;
    }
};