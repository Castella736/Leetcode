class Solution:
    def mySqrt(self, x: int) -> int:
        # Initialize search interval.
        # Initialize mid with Arithmetic-Geometric inequality.
        # The root needs to be in [l,r)
        l, r = 0, (x+1)//2+1;
        
        # Binary search.
        # End when length of search interval <= 1.
        # Otherwise, may occur infinity loop.
        while 1<r-l:
            m = (r+l) // 2;
            res = m*m;
            # Check searching and update.
            if res == x:
                return m;
            elif res > x:
                r = m;
            else:
                l = m;
        
        return l;