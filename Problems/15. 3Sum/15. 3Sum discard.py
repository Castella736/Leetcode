class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # First, sort the list "nums".
        nums.sort();
        last = [];
        ans = [];

        for i in range(1,len(nums)):
            
            l, r = i-1,i+1;
            
            while l>=0 and r<len(nums):
                
                if nums[l]+nums[i]+nums[r] == 0:
                    if [nums[l],nums[i],nums[r]] != last:
                        ans.append( [nums[l],nums[i],nums[r]] );
                        last = [nums[l],nums[i],nums[r]];
                    l -= 1;
                    while nums[l]==nums[l+1] and l>0:
                        l -= 1;
                
                elif nums[l]+nums[i]+nums[r] > 0:
                    l -= 1;
                else:
                    r += 1;
                
        return ans;
        