# include <string>
# include <algorithm>
# include <cstring>
using namespace std;
class Solution {
public:
    int maxLengthBetweenEqualCharacters(string s) {
        int record[26];
        int res = -1;
        std::memset(record, -1, sizeof(record));
        
        for (int i = 0; i < s.length(); i++) {
            if (record[s[i]-'a'] != -1) res = std::max(res, i-record[s[i]-'a']-1);
            else record[s[i]-'a'] = i;
        }

        return res;
    }
};