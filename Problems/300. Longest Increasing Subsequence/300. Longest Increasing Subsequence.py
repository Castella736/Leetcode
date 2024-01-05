from typing import List
class Solution:
    def binarySearch(self, seq: List[int], target: int) -> int:
        l, r = 0, len(seq) - 1
        while l <= r:
            m = (r+l) // 2
            if seq[m] == target:
                return m
            elif seq[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return l
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        layer_min = [nums[0]]
        
        for num in nums:
            pos = self.binarySearch(layer_min, num)
            if pos == len(layer_min): layer_min.append(num)
            else: layer_min[pos] = num
        
        return len(layer_min)