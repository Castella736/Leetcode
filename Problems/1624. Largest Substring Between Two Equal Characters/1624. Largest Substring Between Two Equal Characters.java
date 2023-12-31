import java.util.HashMap;

class Solution {
    public int maxLengthBetweenEqualCharacters(String s) {
        int res = -1;
        HashMap<Character, Integer> record = new HashMap<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (!record.containsKey(ch)) record.put(ch, i);
            else res = Math.max(res, i-record.get(ch)-1);

        }

        return res;
    }
}