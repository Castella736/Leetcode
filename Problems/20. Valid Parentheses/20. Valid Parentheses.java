import java.util.HashMap;
import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        HashMap<Character, Character> table = new HashMap<>();
        Stack<Character> stack = new Stack<>();
        table.put('[', ']');
        table.put('(', ')');
        table.put('{', '}');
        
        for (char ch: s.toCharArray()) {
            if (table.containsKey(ch)) stack.push(ch);
            else {
                if (stack.empty()) return false;
                if (ch != table.get(stack.pop())) return false;
            }
        }

        return stack.empty();
    }
}