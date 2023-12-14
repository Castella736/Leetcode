from collections import deque;
class MinStack:

    def __init__(self):
        self.mainS = deque([]);
        self.minS = deque([]);

    def push(self, val: int) -> None:
        if (not self.mainS or val<=self.getMin()): self.minS.append(val);
        self.mainS.append(val);

    def pop(self) -> None:
        if (self.top() == self.getMin()): self.minS.pop();
        self.mainS.pop();

    def top(self) -> int:
        return self.mainS[-1];

    def getMin(self) -> int:
        return self.minS[-1];


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()