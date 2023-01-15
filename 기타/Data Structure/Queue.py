class Queue():
    def __init__(self, maxSize = 10):
        self.queue = []
        self.maxSize = maxSize
    
    def enqueue(self, data):
        if not self.isFull():
            self.queue.append(data)

    def deque(self):
        if not self.isEmpty():
            return self.queue.pop(0)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        return False

    def isFull(self):
        if len(self.queue) == self.maxSize:
            return True
        return False

queue = Queue()
queue.enqueue(3)
queue.enqueue(5)
queue.enqueue(6)
print(queue.deque())
print(queue.deque())