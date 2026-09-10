import math

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = math.inf
        self.prev_min = math.inf
        
    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack:
            self.min_stack.append(val)
            return
        if val <= self.min_stack[-1]:
            self.min_stack.append(val)
            return
        # self.prev_min = min(self.min_val, self.prev_min)
        # self.min_val = min(val, self.min_val)

    def pop(self) -> None:
        popped = self.stack.pop()
        
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        # print("self.stack: ")
        # print(self.stack)

        # print("self.min_stack: ")
        # print(self.min_stack)

        # print("------------")
        if self.min_stack:
            return self.min_stack[-1]
        else:
            print("Nothing in min stack: ")
            print(self.min_stack)

        
