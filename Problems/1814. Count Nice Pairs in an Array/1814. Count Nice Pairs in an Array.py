from collections import defaultdict;
class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        
        # Auxiliary function to reverse int.
        def rev(num: int) -> int:
            return int(
                str(num)[::-1]
            );
        
        res = 0; # Record the result.
        m = int(1e9) + 7; # Moduler.
        table = defaultdict(int); # Help to record f(num) = num - rev(num).
        
        # Record all seen "num - rev(num)".
        for num in nums:
            f = num - rev(num);
            table[f] += 1;
        
        # Since the pair require i < j.
        for f in table:
            res += (table[f]*(table[f]-1))//2;
            res %= m;
        
        return res;