class Solution {
public:
    int distinctIntegers(int n) {
        return std::max({n-1, 1});
    }
};