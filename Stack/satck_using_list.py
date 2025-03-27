class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
        return f"{element} pushed on to the stack"
    def is_empty(self):
        if self.stack:
            return 'Stack is not empty'
        else:
            return 'Stack is empty'
    def pop(self):
        if self.stack:
            res=self.stack.pop(-1)
            return f'{res} is removed'
        else:
            return 'Stack is empty'
    def size(self):
        return f"Size if stack is {len(self.stack)}"
    
    def peek(self):
        return f'Peek item is {self.stack[-1]}'

obj = Stack()
print(obj.push(10))
print(obj.push(20))
print(obj.push(50))
print(obj.pop())
print(obj.is_empty())

