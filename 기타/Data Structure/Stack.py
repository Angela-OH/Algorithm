class Stack():
    def __init__(self, maxSize = 10):
        self.stack = []
        self.maxSize = maxSize

    def push(self, data):
        if not self.isFull():
            self.stack.append(data)

    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()

    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]

    def isEmpty(self):
        if len(self.stack) == 0:
            return True
        return False

    def isFull(self):
        if len(self.stack) == self.maxSize:
            return True
        return False

stack = Stack(5)
stack.push(2)
stack.push(4)
stack.push(6)
print(stack.pop())
print(stack.pop())
