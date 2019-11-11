class Deque(object):

    def __init__(self):
        self.items = []

    def addRear(self,item):
        self.items.insert(0,item)

    def addFront(self,item):
        self.items.append(item)

    def removeRare(self):
        self.items.pop(0)

    def removeFront(self):
        self.items.pop()

    def isEmpty(self):
        return self.items == []

    def display(self):
        return self.items

    def size(self):
        return  len(self.items)

d = Deque()
print(d.isEmpty())
print(d.display())

d.addRear(1)
print("The current size of deque is {} and stack elements {}".format(d.size(),d.display()))
d.addRear(2)
print("The current size of deque is {} and stack elements {}".format(d.size(),d.display()))
d.addFront(4)
print("The current size of deque is {} and stack elements {}".format(d.size(),d.display()))
d.addFront(5)
print("The current size of deque is {} and stack elements {}".format(d.size(),d.display()))
