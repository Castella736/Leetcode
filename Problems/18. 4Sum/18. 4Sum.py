class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Claim variables.
        L = len(nums);
        res = [];
        
        # Sort data.
        nums.sort();
        
        # Use nested loop to reduce to 2Sum problem
        for i in range(L):
            # Skip for same num
            if i>0 and nums[i] == nums[i-1]:
                continue;
            for j in range(i+1,L):
                # Skip for same num
                if j>i+1 and nums[j] == nums[j-1]:
                    continue;
                
                # Reduce to 2Sum problem.
                l,r = j+1, L-1;
                while l<r:
                    sum = nums[i]+nums[j]+nums[l]+nums[r];
                    
                    if sum==target:
                        res.append([nums[i],nums[j],nums[l],nums[r]]);
                        l += 1;
                        while l<r and nums[l]==nums[l-1]:
                            l += 1;
                    elif sum>target:
                        r -= 1;
                    else:
                        l += 1;
                        
        return res;
    
# test.