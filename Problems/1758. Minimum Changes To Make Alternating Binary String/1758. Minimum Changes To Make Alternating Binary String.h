# include <string>
using namespace std;
class Solution {
public:
    int minOperations(string s) {
        int cost = 0; // cost of change the string to 0 start alternating string.
        for (int i = 0; i < s.length(); i++) {
            if (s[i] != '0'+(i%2)) cost++;
        }

        return (cost < s.length()-cost) ? cost : s.length()-cost;
    }
};