from collections import defaultdict
from typing import List
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = defaultdict(int)
        res = 0
        
        for num in nums:
            count[num] += 1
        for num in count:
            if count[num] == 1: return -1
            res += (count[num]+2) // 3
        
        return res