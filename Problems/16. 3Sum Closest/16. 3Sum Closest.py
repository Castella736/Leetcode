class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort();
        i,l,r = 0,1,2;
        best = nums[i]+nums[l]+nums[r];

        for i,num in enumerate(nums):
            # skip if there's consecutive same number.
            if nums[i-1]==num:
                continue;
            
            l, r = i+1,len(nums)-1;
            
            while l<r:
                sum = nums[l]+num+nums[r];
                # check if new sum better.
                if abs(sum-target) < abs(best-target):
                    best = sum;
                
                # compare sum-target to 0.
                if sum-target == 0:
                    return sum;    
                elif sum-target > 0:
                    r -= 1;
                    while nums[r]==nums[r+1] and l<r:
                            r -= 1;
                else:
                    l += 1;
                    while nums[l]==nums[l-1] and l<r:
                            l += 1;
                            
        return best;