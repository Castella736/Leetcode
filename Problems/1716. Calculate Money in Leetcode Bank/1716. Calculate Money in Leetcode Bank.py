class Solution:
    def totalMoney(self, n: int) -> int:
        w = n // 7; # Passed weeks.
        l = n % 7; # Remain days.
        res = 21*w + 7*sum(range(w+1));
        
        res += l*w + sum(range(l+1));
        
        return res;