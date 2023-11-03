class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Record number of occurences of each number
        rec = {};
        for ele in arr:
            if not ele in rec:
                rec[ele] = 0;
            rec[ele] += 1;
        # List all occurences and sort them.
        # So that we can compare them.
        occ = [rec[ele] for ele in rec];
        occ.sort();
        
        for i in range(1, len(occ)):
            if occ[i] == occ[i-1]:
                return False;
        
        return True;