class Queue(object):

    def __init__(self):
        self.items = []

    def push(self,element):
        self.items.insert(0,element)

    def pop(self):
        self.items.pop()

    def display(self):
        return self.items

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

q = Queue()
print(q.isEmpty())
q.push(1)
q.push("Gopi")
q.push(True)
print(q.display())
q.pop()
print(q.display())
q.pop()
print(q.display())

print(q.isEmpty())