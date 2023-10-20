class Solution:
    # Augmented function to calcualte median of a sequence
    def calcMedian(self, nums: List[int]) -> float:
        n = len(nums);
        if n%2 == 1:
            return float( nums[n//2] );
        else:
            return ( nums[n//2-1] + nums[n//2] ) / 2;

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Calcualte the length of the sequences.
        n = len(nums1);
        m = len(nums2);
        
        # End point cases.
        nums = nums1 + nums2;
        nums.sort();
        if n <= 2 or m <= 2:
            return self.calcMedian( nums );
        
        med1 = self.calcMedian(nums1);
        med2 = self.calcMedian(nums2);
        
        # Compare medians.
        # If equal, return median.
        if med1-med2 > 0 and med1-med2 < 0.4:
            return med1;
        elif med2-med1 > 0 and med2-med1 < 0.4:
            return med2;
        # May assume med1 <= med2
        elif med1 > med2:
            return self.findMedianSortedArrays(nums2, nums1);
        else:
            d_length = min(n//2,m//2);
            nums1[:] = nums1[d_length:];
            nums2[:] = nums2[:-d_length];
            
            return self.findMedianSortedArrays(nums1,nums2);