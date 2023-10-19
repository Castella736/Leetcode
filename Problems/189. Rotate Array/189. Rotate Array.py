import math;

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        # Let k mod length of nums, n
        n = len(nums);
        k = k % n;
        
        for start in range(math.gcd(n,k)):
            current = start;
            trip_val = nums[current];
            
            while True:
                next = (current+k) % n;
                current = next;
                
                temp = nums[next];
                nums[next] = trip_val;
                trip_val = temp;
                
                if current == start:
                    break;
        
        return None;