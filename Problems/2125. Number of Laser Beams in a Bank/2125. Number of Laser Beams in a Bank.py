from typing import List
class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        res = 0
        prev_count = 0
        cur_count = 0
        
        for row in bank:
            cur_count = row.count('1')
            if cur_count > 0:
                res += prev_count * cur_count
                prev_count = cur_count
        
        return res