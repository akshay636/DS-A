from collections import deque
class Stack:
  
  def __init__(self):
    self.container = deque()
    
  def push(self,value):
    self.container.append(value)
    
  def pop(self):
   return self.container.pop()

  def peek(self):
   return self.container[-1]
  
  def size(self) -> int:
   return len(self.container)
 
stack = Stack()
s = 'i will crack google'

for i in s:
  stack.push(i)
rev =''
for j in range(0, stack.size()):
  rev += stack.pop()
  
print(rev)