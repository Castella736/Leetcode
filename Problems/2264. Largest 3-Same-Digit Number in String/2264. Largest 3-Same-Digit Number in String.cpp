class Solution {
public:
    string largestGoodInteger(string num) {
        char res = -1;
        char prev = -1;
        short counter = 1;

        for(char digit: num){
            if(digit == prev){
                counter += 1;
                if(counter == 3){
                    res = std::max(digit, res);
                }
            }
            else{
                prev = digit;
                counter = 1;
            }
        }

        if(res < 0) return "";
        return string(3, res);
    }
};