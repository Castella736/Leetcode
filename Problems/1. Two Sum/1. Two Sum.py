from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash table.
        record = {};
        for index, num in enumerate(nums):
            if num in record:
                return [record[num], index];
            else:
                record[target-num] = index;