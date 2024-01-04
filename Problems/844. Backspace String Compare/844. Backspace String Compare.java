class Solution {
    private int nextValidPos(String s, int p) {
        int back = 0;
        while (p >= 0) {
            if (s.charAt(p) == '#') back++;
            else {
                if (back > 0) back--;
                else break;
            }
            p--;
        }
        return p;
    }

    public boolean backspaceCompare(String s, String t) {
        int p = s.length()-1;
        int q = t.length()-1;

        while (p >= 0 || q >= 0) {
            p = nextValidPos(s, p);
            q = nextValidPos(t, q);

            if (p < 0 && q < 0) return true;
            else if (p < 0 || q < 0) return false;
            if (s.charAt(p) != t.charAt(q)) return false;
            p--;
            q--;
        }

        return true;
    }
}