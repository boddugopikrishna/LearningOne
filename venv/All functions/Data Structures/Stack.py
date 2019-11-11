class Empty(Exception):
    """
    Error attempting to access an element from an empty container.
    """
    pass

class Stack():
    '''Stack is a collection of objects that are inserted and removed accoding to the
last-in,first-out(LIFO) priciple'''
    def __init__(self):
        '''Create an Empty stack'''
        self.data = []

    def __len__(self):
        '''Return the number of elements in the stack'''
        return len(self.data)

    def is_empty(self):
        '''Return True if the stack is empty'''
        return  len(self.data) == 0

    def Push(self,e):
        '''Add an element e to the top of the stack'''
        self.data.append(e)  #new item stored at end of list

    def top(self):
        """Return the element at the top of the list"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.data[-1]

    def pop(self):
        """
        Remove and return the element firm the top of the stack
        Raise Empty exception if the stack is empty
        """
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self.data.pop()

