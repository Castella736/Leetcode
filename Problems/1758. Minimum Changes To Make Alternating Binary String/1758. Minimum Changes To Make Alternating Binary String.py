class Solution:
    def minOperations(self, s: str) -> int:
        def countCost(s: str, flag: str):
            res = 0
            for bit in s:
                if bit != flag: res += 1
                flag = '0' if flag == '1' else '1'
                
            return res
        
        return min(countCost(s, '0'), countCost(s, '1'))