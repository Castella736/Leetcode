class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        record = {}
        res = -1
        
        for i in range(len(s)):
            if s[i] in record: res = max(res, i-record[s[i]]-1)
            else: record[s[i]] = i
        
        return res