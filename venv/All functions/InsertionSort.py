import timeit
class Queue(object):

    def __init__(self):
        self.items = []

    def frontPush(self,index,item):
        self.items.insert(index,item)

    def rearPush(self,item):
        self.items.append(item)

    def display(self):
        return self.items


def sort(l):
    q= Queue()
    length = len(l)
    for val in range(length):
        min_val = min(l)
        q.rearPush(min_val)
        l.pop(l.index(min_val))
    return q.display()

l = [5,7,1,8,2,9,3,6,4]
start_time = timeit.default_timer()
sort(l)
print(timeit.default_timer() - start_time)





