class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort();
        ans = [];

        for i,num in enumerate(nums):
            if i>0 and nums[i-1]==num:
                continue;
            
            l, r = i+1,len(nums)-1;
            
            while l < r:
                sum = nums[l]+num+nums[r];
                
                if sum == 0:
                    ans.append( [nums[l],num,nums[r]] );
                    l += 1;
                    while nums[l]==nums[l-1] and l<r:
                        l += 1;
                
                elif sum > 0:
                    r -= 1;
                else:
                    l += 1;
                
        return ans;
        