class Solution:
    def maxScore(self, s: str) -> int:
        l_comp = 1 if s[0] == '0' else 0
        best_l_comp = l_comp
        num_ones = 0
        for bit in s[1:-1]:
            if bit == '0':
                l_comp += 1
                best_l_comp = max(l_comp, best_l_comp)
            else:
                l_comp -= 1
                num_ones += 1
        num_ones += 1 if s[-1] == '1' else 0
        
        return best_l_comp + num_ones