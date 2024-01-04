# include <string>
using namespace std;
class Solution {
private:
    void nextValidPos(string s, int& p) {
        int back = 0;
        while (p >= 0) {
            if (s[p] == '#') back++;
            else {
                if (back > 0) back--;
                else break;
            }
            p--;
        }
    }

public:
    bool backspaceCompare(string s, string t) {
        int p = s.length() - 1;
        int q = t.length() - 1;

        while (p >= 0 || q >= 0) {
            nextValidPos(s, p);
            nextValidPos(t, q);

            if (p < 0 && q < 0) return true;
            else if (p < 0 || q < 0) return false;
            if (s[p--] != t[q--]) return false;
        }

        return true;
    }
};