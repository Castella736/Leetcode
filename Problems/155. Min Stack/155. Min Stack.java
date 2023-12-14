import java.util.EmptyStackException;
import java.util.Stack;

class MinStack {

    private Stack<Integer> S = new Stack<>();
    private Stack<Integer> minS = new Stack<>();

    public MinStack() { }
    
    public void push(int val) {
        if (minS.size() == 0) minS.push(val);
        else if (val <= getMin()) minS.push(val);
        S.push(val);
    }
    
    public void pop() {
        if (S.size() == 0) throw new EmptyStackException();
        if (S.peek() == getMin()) minS.pop();
        S.pop();
    }
    
    public int top() {
        if (S.size() == 0) throw new EmptyStackException();
        return S.peek();
    }
    
    public int getMin() {
        if (S.size() == 0) throw new EmptyStackException();
        return minS.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */