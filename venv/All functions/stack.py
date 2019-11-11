class stack(object):

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return  self.items == []

    def push(self,element):
        self.items.append(element)

    def pop(self):
        self.items.pop()

    def size(self):
        return  len(self.items)

    def peek(self):
        return  self.items[len(self.items)-1]

s = stack()
print(s.isEmpty())
s.push("two")
print(s.isEmpty())
print(s.peek())