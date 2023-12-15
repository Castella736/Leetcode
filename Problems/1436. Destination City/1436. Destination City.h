# include <unordered_set>
# include <vector>
# include <string>
using namespace std;

class Solution {
public:
    string destCity(vector<vector<string>>& paths) {
        unordered_set<string> departure;
        for (const vector<string>& path: paths)
            departure.insert(path[0]);

        for (const vector<string>& path: paths)
            if (departure.find(path[1]) == departure.end())
                return path[1];
        
        return "";
    }
};