from typing import List;
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def root(i):
            nonlocal id;
            while i != id[i]:
                id[i] = id[id[i]];
                i = id[i];
            
            return i;
        
        def union(p, q):
            nonlocal sz;
            p = root(p);
            q = root(q);
            
            if p != q:
                if sz[p] < sz[q]:
                    p, q = q, p;
                id[q] = p;
                sz[p] += sz[q];
        
        if not nums:
            return 0;
        
        nums = list(set(nums)); # remove duplicated numbers.
        nums = {num: i for i, num in enumerate(nums)}; # record index of each numbers.
        # Usual weighted-union-find structure with path compression.
        id = [i for i in range(len(nums))]; 
        sz = [1 for _ in range(len(nums))];
        
        # Connecting numbers if their difference is 1.
        # So if two numbers are in a same component,
        # they are in a same consecutive numbers.
        for num in nums:
            if num-1 in nums:
                union(nums[num], nums[num-1]);
            if num+1 in nums:
                union(nums[num], nums[num+1]);

        # Return the size of maximum component.
        return max(sz);
    
    def longestConsecutive(self, nums: List[int]) -> int:
        max_streak = 0; # Record max streak.
        cur_streak = 0; # Record current streak.
        nums = set(nums); # Remove duplicated elements
        
        # Traverse the set of nums.
        for num in nums:
            cur_streak = 1;
            # If the num is start of some consecutive sequence in nums.
            if num-1 not in nums:
                x = num;
                
                # Track the maximum streak of num.
                while x+1 in nums:
                    cur_streak += 1;
                    x += 1;
                
                # Compare the result to the record.
                max_streak = max(cur_streak, max_streak);
        
        # Return the result.
        return max_streak;