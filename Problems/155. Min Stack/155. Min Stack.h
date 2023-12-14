# include <stack>
using namespace std;
class MinStack {
private:
    stack<int> mainStack;
    stack<int> minStack;

public:
    MinStack() { }
    
    void push(int val) {
        if (mainStack.empty() || val<=getMin()) minStack.push(val);
        mainStack.push(val);
    }
    
    void pop() {
        if (mainStack.top() == getMin()) minStack.pop();
        mainStack.pop();
    }
    
    int top() { return mainStack.top(); }
    
    int getMin() { return minStack.top(); }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */