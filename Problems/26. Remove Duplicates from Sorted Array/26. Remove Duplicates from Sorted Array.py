class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr, check = 1,1;

        if len(nums)==1:
            return 1;

        while check < len(nums):
            if nums[curr-1]<nums[check]:
                nums[curr]=nums[check];
                curr += 1;
                check += 1;
            else:
                check += 1;

        return curr;