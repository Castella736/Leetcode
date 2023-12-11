class Solution {
    public int findSpecialInteger(int[] arr) {
        // Exclude singleton array.
        if (arr.length == 1) return arr[0];

        // Set counter.
        int COUNT = arr.length / 4;
        int curStreak = 1;

        for (int i = 1; i < arr.length; i++) {
            if (arr[i] == arr[i-1]) {
                curStreak++;
                if (curStreak > COUNT) return arr[i];
            }
            else {
                curStreak = 1;
            }
        }

        return -1;
    }
}