class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Length of nums
        n = len(nums);
        # Record sum of each side.
        # l_sum[k] = sum to k-th index(not included) from the left.
        # r_sum[k] = sum to k-th index(not included) from the right.
        l_sum, r_sum = {0:0}, {n-1:0};
        for i in range(1,n):
            l_sum[i] = l_sum[i-1] + nums[i-1];
            r_sum[n-1-i] = r_sum[n-i] + nums[n-i];
        
        # Check if pivot exists.
        for i in range(n):
            if l_sum[i] == r_sum[i]:
                return i;
        return -1;