class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # candidate to be swapped.
        s = 0;
        for i in range(len(nums)):
            # swap if find zero.
            if nums[i]!=0:
                nums[s], nums[i] = nums[i], nums[s];
                # look next candidate.
                s += 1;
            # If the loop ends, the sorting is done.
        
        return None;