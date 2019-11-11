nums = [val for val in range(9)]
print(nums)

class stack():

    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)

def reverse(sequence):
    s = stack()
    revers = []
    for val in sequence:
        s.push(val)
    while s.__len__() != 0:
        revers.append(s.pop())
    return "".join(revers)
print(reverse("Gopi krishna"))