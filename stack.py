#stack implementation using list 

class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if len(self.stack) == 0:
            return "stack is empty"
        return self.stack.pop()

    def isEmpty(self):
        return len(self.stack) == 0
    
    def size(self):
        return len(self.stack)
    
    def peek(self):
        if len(self.stack) == 0:
            return "stack is empty"
        return self.stack[-1]
    
# Creating  a stack
myStack = Stack()

myStack.push('A')
myStack.push('B')
myStack.push('C')

print("Stack: ", myStack.stack)

print("Pop: ", myStack.pop())

print("Peek: ", myStack.peek())

print("isEmpty: ", myStack.isEmpty())

print("Size: ", myStack.size())