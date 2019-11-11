class stack():

    def __init__(self):
        self.data = []

    def push(self,item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()
opertaions = ["E","A","S","*","Q","U","E","*","*","*","S","T","*","*","*","I","O","*","N","*","*","*"]
def stackOperations(listOfOperations):
    s = stack()
    pop_list = []
    for val in listOfOperations:
        if val != "*":
            s.push(val)
        else:
            pop_list.append(s.pop())
    return pop_list
print(stackOperations(opertaions))

