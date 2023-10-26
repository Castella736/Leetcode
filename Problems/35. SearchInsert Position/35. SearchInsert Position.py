class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointer
        l, r = 0, len(nums)-1;
        
        # Exhausting array through binary search
        while l <= r:
            p = (r+l) // 2;
            if nums[p] == target:
                return p;
            elif nums[p] > target:
                r = p-1;
            else:
                l = p+1;
        
        # End case
        return l;