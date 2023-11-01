class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Initial answer.
        res = 0;
        # Sort nums so that we can perform left-right pointers search.
        nums.sort();

        # Main left-right pointers search.
        l, r = 0, len(nums)-1;
        # The advances of pointers work in spirit of popping seen elements.
        while l<r:
            # Riemann summantion.
            if nums[l]+nums[r] == k:
                res += 1;
                l += 1;
                r -= 1;
            elif nums[l]+nums[r] > k:
                r -= 1;
            else:
                l += 1;
        
        return res;