class Solution {
    public int maxProduct(int[] nums) {
        int maxVal = -1;
        int sMaxVal = -1;
        for (int num: nums) {
            if (num >= maxVal) {
                sMaxVal = maxVal;
                maxVal = num;
            }
            else if (num > sMaxVal){
                sMaxVal = num;
            }
        }

        return (sMaxVal - 1) * (maxVal - 1);
    }
}