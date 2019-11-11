class stack(object):
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def display(self):
        return self.items

    def get_item(self,index):
        return self.items[index]
str = '{(([])[])[]]}'
s = stack()
for val in str:
    #print(val)
    if val in '[{(':
        s.push(val)
        print(s.display())
    else:
        output = s.pop()
        print(output)
        if (output,val) in [('[',']'),('{','}'),('(',')')]:
            print((output, val))
            print(True)
        else:
            print(False)


'''def isBalanced(s):
    if len(s) % 2 != 0:
        return "NO"
    stack = []
    for val in s:
        print(val)
        if val in '[{(':
            stack.append(val)
        else:
            if len(stack) == 0:
                return "NO"
            output = stack.pop()
            if (output,val) not in [('[',']'),('{','}'),('(',')')]:
                return "NO"
    return "YES"
    '''