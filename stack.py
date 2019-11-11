class stack:
    def __init__(self,max_size):
        self.max_size = max_size
        self._elements = [None]*self.max_size
        self._top = -1

    def get_max_size(self):
        return self.max_size
    def is_full(self):
        return True
    def push(self,data):
        if(self.is_full()):
            return "Stack is full"
        else:
            self._top += 1
            self._elements = data

