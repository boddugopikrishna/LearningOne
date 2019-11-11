class Queue(object):

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def display(self):
        return self.items[0]

queries = []
for _ in range(10):
    queries.append(list(map(int, input().rstrip().split())))
queue = Queue()
for val in queries:
    if val[0] == 1:
        queue.enqueue(val[1])
    elif val[0] == 2:
        queue.dequeue()
    else:
        print(queue.display())


#print(queries)

