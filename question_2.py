class Stack:
    def __init__(self):
        self.stack = list()

    def find(self, element):
        tmp = self.stack[len(self.stack):None:-1]
        return tmp.index(element)
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if (self.isEmpty()):
            return "Error! Stack is empty!"
        else: 
            return self.stack.pop()
        
    def size(self):
        return len(self.stack)
        
    def isEmpty(self):
        return len(self.stack) == 0
    
    def __str__(self):
        res = ""
        for i in self.stack:
            res += str(i) + ', '
        return res
