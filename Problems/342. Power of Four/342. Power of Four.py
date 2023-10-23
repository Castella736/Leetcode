class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # n can't be power of 4 if it is non-positive.
        if n<=0:
            return False;
        
        # let n be modded by 4 recursively until it is 1. (return True;)
        # Or until its remainder is not 0. (return False;)
        while True:
            if n == 1:
                return True;
                
            elif n%4 != 0:
                return False;
            
            n = n//4;