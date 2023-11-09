class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,m = len(s2), len(s1); # length of s2, s1 respectively.
        table = {}; # Use a hash table to store occurrencies of char. in s1.
        
        # Exclude case that |s1| > |s2|.
        if n<m:
            return False;
        
        # Function to help check if is substring.
        def checkExist(table: dict) -> bool:
            for key in table:
                if table[key] < 0:
                    return False;
            return True;
        
        # Calculate occurrency of char. in s1
        for char in s1:
            if char in table:
                table[char] -= 1;
            else:
                table[char] = -1;
        
        # Construct a window function start with s2[0:m].
        # Check if the window is permutation similar to s1.
        for i in range(m):
            if s2[i] in table:
                table[s2[i]] += 1;
        if checkExist(table)==True:
            return True;
        
        # Moving the window function and conduct checking.
        i = 0;
        while i+m < n:
            if s2[i+m] in table:
                table[s2[i+m]] += 1;
            if s2[i] in table:
                table[s2[i]] -= 1;
            
            if checkExist(table)==True:
                return True;
            i += 1;
        
        return False;