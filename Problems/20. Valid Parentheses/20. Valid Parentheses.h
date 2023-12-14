# include <unordered_map>
# include <string>
# include <stack>
using namespace std;

class Solution {
public:
    bool isValid(string s) {
        unordered_map<char, char> table = {
            {'(', ')'},
            {'[', ']'},
            {'{', '}'},
        };
        stack<char> seen;

        for (char ch: s) {
            if (table.find(ch) != table.end()) seen.push(ch);
            else {
                if (seen.empty()) return false;
                char top = seen.top();
                seen.pop();
                if (ch != table[top]) return false;
            }
        }

        return seen.empty();
    }
};