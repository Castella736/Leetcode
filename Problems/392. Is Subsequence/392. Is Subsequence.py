class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Use `check` to track each element in s.
        # Look at next element if finded in s.
        check = 0;
        m = len(s);
        
        # Exclude empty seq.
        if m == 0:
            return True;
        
        for i in range(len(t)):
            if t[i] == s[check]:
                check += 1;
                if check == m:
                    return True;
        
        return False;