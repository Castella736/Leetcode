# include <string>
# include <unordered_map>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> table;
        for (int i = 0; i < s.size(); i++) {
            table[s[i]]++;
            table[t[i]]--;
        }

        for (auto& ch: table)
            if (ch.second != 0) return false;
        
        return true;
    }
};