import java.lang.Math;
class Solution {
    public int minOperations(String s) {
        int cost = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != '0'+(i%2)) cost++;
        }

        return Math.min(cost, s.length()-cost);
    }
}