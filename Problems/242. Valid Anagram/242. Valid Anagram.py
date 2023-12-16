from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        table = defaultdict(int)
        
        for i in range(len(s)):
            table[s[i]] += 1
            table[t[i]] -= 1
            
        for ch in table:
            if table[ch] != 0: return False
            
        return True