class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums);
        # Exclude singleton list.
        if n == 1:
            return 1;
        
        # Sort the nums.
        nums.sort();

        res = 1;
        l, r = 0, 1;
        base = nums[l]; # base = sum(nums[l:r])
        
        # The positions of point of the solution are always contiguous.
        # This can be proven.
        # The gap it takes to fill the positions are
        # sum ( b_m - b_i ) where b_m is the last num in the tuple.
        # So it's actually (r-l)*b_m - (b_l+b_{l+1}+...+b_{m-1}).
        for r in range(1,n):
            cur_mass = (r-l)*nums[r] - base;
            if cur_mass <= k:
                res = max(r-l+1, res);
            else:
                base -= nums[l];
                l += 1;

            base += nums[r];
        
        return res;