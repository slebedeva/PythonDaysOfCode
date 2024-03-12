# Create a program to implement a stack using a list

# Stack is like a stack of plates: last in, first out
# Methods: push, pop, top, isEmpty, size
# Stack overflow is when the allowed size is exceeded (memory allocation usage)
# Stack with dynamic size is implemented using linked list #TODO
# Examples: redo-undo, browser arrows, chess & similar games, tree traversal, tower of hanoi
# https://www.geeksforgeeks.org/introduction-to-stack-data-structure-and-algorithm-tutorials/

class Stack:
    def __init__(self, stack = []) -> None:
        self.stack = stack
    
    def push(self, item):
        self.stack.append(item)
    def pop(self):
        if not self.isEmpty():
            item = self.stack.pop()
        else: 
            item = None
        return item
    
    def top(self, n=5):
        return self.stack[-n:]

    def isEmpty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
