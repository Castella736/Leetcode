class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort();
        
        i,r,l = 0,1,2;
        best = nums[i]+nums[r]+nums[l];

        for i,num in enumerate(nums):
            if i>0 and nums[i-1]==num:
                continue;
            
            l, r = i+1,len(nums)-1;
            
            while l<r:
                sum = nums[l]+num+nums[r];
                if abs(sum-target) < abs(best-target):
                    best = sum;
                
                if sum-target == 0:
                    return sum;    
                elif sum-target > 0:
                    r -= 1;
                else:
                    l += 1;
                
        return best;