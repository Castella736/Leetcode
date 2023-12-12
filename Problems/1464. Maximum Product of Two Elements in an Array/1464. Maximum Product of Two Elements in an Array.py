class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxVal = -1;
        sMaxVal = -1;
        for num in nums:
            if (maxVal < sMaxVal): maxVal, sMaxVal = sMaxVal, maxVal;
            sMaxVal = max(num, sMaxVal);
            
        return (maxVal - 1) * (sMaxVal - 1);