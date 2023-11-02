class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        table1, table2 = set(), set();
        ans = [[],[]];
        
        for ele in nums1:
            if not ele in table1:
                table1.add(ele);
        for ele in nums2:
            if not ele in table2:
                table2.add(ele);
        
        ans[0][:] = list(table1.difference(table2));
        ans[1][:] = list(table2.difference(table1));
        
        return ans;