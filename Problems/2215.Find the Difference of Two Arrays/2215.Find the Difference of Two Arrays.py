class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1 = set([nums1];
        table2 = set([nums2];
        return [list(table1-table2), list(table2-table1)];