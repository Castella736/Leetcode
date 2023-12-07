class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num), 0, -1):
            if num[i-1] in {'1','3','5','7','9'}:
                return num[:i];
        
        return "";