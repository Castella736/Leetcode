class RecentCounter:
    
    def __init__(self):
        # queue of int store pings associated with time.
        self.rec = [];

    def ping(self, t: int) -> int:
        # Include the last ping.
        self.rec.append(t);
        
        # Eliminate outdated points.
        while self.rec[0] < t-3000:
            self.rec.pop(0);
        
        return len(self.rec);

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)