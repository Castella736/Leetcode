class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        COUNT = len(arr) // 4;
        for i in range(len(arr) - COUNT):
            if arr[i] == arr[i+COUNT]:
                return arr[i];