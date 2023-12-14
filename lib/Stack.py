class Stack:
    def __init__(self, items=[], limit=100):
        self.items = []
        self.limit = limit

        for item in items:
            if not self.full():
                self.items.append(item)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return None
        return self.items.pop()

    def peek(self):
        pass

    def size(self):
        return len(self.items)

    def full(self):
        return self.size() >= self.limit

    def search(self, target):
        try:
            index = self.items.index(target)
            return self.size() - index - 1
        except:
            return -1
