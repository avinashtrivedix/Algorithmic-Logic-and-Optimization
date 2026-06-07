# design a stach that supports standarad operations pushm poop, top and get_min.
# method 1 - loop through the stack to find the minimum value when get_min is called. 
# this method is often not efficientn because the time complexity will be O(N)

class MinStack:
    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, x: int) -> None:
        self.main_stack.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            current_min = self.min_stack[-1]
            self.min_stack.append(min(x, current_min))  

    def pop(self)  -> None:
        if not self.main_stack:
            return None
        self.main_stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        if not self.main_stack:
            return None
        return self.main_stack[-1]

    def get_min_inneficient(self) -> int:
        if not self.main_stack:
            return None
        return min(self.main_stack)
    
    def get_min(self) -> int:
        if not self.min_stack:
            return None
        return self.min_stack[-1]
    

if __name__ == "__main__":
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    print(stack.get_min())
    print(stack.top())