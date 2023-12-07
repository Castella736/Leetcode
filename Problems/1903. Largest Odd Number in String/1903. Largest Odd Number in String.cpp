# include <string>
using namespace std;
class Solution {
public:
    string largestOddNumber(string num) {
        cin.tie(0);
        ios_base::sync_with_stdio(0);
        for (int i=num.size()-1; i >= 0; i--){
            if (num[i] & 1){
                return num;
            }
            else{
                num.pop_back();
            }
        }

        return "";
    }
};