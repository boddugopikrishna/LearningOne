class Node():
    def __init__(self,data = None):
        self.data = data
        self.next = None

class SingleLinkedList():
    def __init__(self):
        self.head = None

    def traverseList(self):
        print_val = self.head

        while print_val is not None:
            print(print_val.data)
            print_val = print_val.next

    #Update the new nodes next val to existing node
    def insert_val_At_begining (self,new_data):
        new_Node = Node(new_data)
        new_Node.next = self.head
        self.head = new_Node

    def insert_val_At_End(self,new_data):
        new_Node = Node(new_data)
        #If linkedList is empty,insert node at head level
        if self.head is None:
            self.head = new_Node
            return
        #decalring variable for last node in linkedlist
        laste = self.head
        while laste.next:
            laste =laste.next
        laste.next = new_Node

        #Inserting in between two data Nodes

    def in_between(self,middle_node,new_data):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        new_Node = Node(new_data)
        new_Node.next = middle_node.next
        middle_node.next = new_Node

    def remove_Node(self,remove_key):
        head_val = self.head

        if head_val is not None:
            if head_val.data == remove_key:
                self.head = head_val.next
                head_val = None
                return
        while head_val is not None:
            if head_val.data == remove_key:
                break
            prev = head_val
            head_val = head_val.next

        if head_val ==  None:
            return
        prev.next = head_val.next

        head_val = None





s = SingleLinkedList()
s.insert_val_At_begining("At Begining")
s.traverseList()
