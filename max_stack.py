class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack =[]

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        return self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def peekMax(self) -> int:
        return max(self.stack)

    def popMax(self) -> int:
        rev = self.stack[::-1]
        m = max(rev)
        i = rev.index(m)
        i = len(self.stack) - 1 - i
        # print(i)
        return self.stack.pop(i)


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()