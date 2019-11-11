class Node(object):

    def __init__(self,v=None):
        self.value = v
        self.next = None

    def isEmpty(self):
        if self.value == None:
            return True
        else:
            return False

    def append(self,v):
        #If List is Empty
        if self.isEmpty() == True:
            self.value = v
        # If pointer is none : either at begining or at end
        elif self.next == None:
            newNode = Node(v)
            self.next = newNode
        else:
            self.next.append(v)
        return ()

    def insert(self,v):

        if self.value == None:
            self.value = v
            return
        newNode = Node(v)

        #Exchange values in self and new node
        (self.value,newNode.value) = (newNode.value,self.value)
        (self.next,newNode.next) = (newNode,self.next)
        return

    def delete(self,v):
        if self.isEmpty():
            return
        if self.value == v:
            self.value = None
            if self.next != None:
                self.value = self.next.value
                self.next = self.next.next
                return
        else:
            if self.next != None:
                self.next.delete(v)
                if self.next.value == None:
                    self.next = None
        return

    def __str__(self):
        selfList = []
        if self.value == None:
            return (str(selfList))
