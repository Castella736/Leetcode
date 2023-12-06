class Solution:
    def largestGoodInteger(self, num: str) -> str:
        res = -1;
        prev = None;
        counter = 0;
        
        for digit in num:
            if digit == prev:
                counter += 1;
                if counter == 3:
                    res = max(int(digit), res);
            else:
                prev = digit;
                counter = 1;
                
        return (
            "" if res < 0 else str(res)*3
        );