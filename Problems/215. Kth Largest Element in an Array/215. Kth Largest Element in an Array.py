import heapq;
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k] # Create a heap of length k.
        heapq.heapify(heap);
        
        # Heap sorting.
        for num in nums[k:]:
            if num > heap[0]:
                heapq.heapreplace(heap, num);
        
        return heap[0];