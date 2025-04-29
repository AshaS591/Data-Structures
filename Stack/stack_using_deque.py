from collections import deque

class Stack:
    def __init__(self):
        self.stack=deque()
       
    def push(self,data):
        self.stack.append(data)
        print(f'{data} pushed on to the stack successfully...')
    def pop(self):
        res=self.stack.pop()
        print(f'{res} is removed from stack successfully...')
    def is_empty(self):
        if len(self.stack)==0:
            print('Stack is empty')
        else:
            print('Stack is not empty...')
    def peek(self):
        print(f'Top element of stack {self.stack} is {self.stack[-1]}')
    def size(self):
        print(f'Size of stack {self.stack} is {len(self.stack)}')
            
stack =Stack()
stack.push(10)
stack.push(20)
stack.push(40)
stack.size()
stack.is_empty()
stack.push(60)
stack.push(90)
stack.pop()

