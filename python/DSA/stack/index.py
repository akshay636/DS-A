class Stack:
  def __init__(self):
    self.container = []
    
  def push(self, value):
    self.container.append(value)
    
  def pop(self):
    return self.container.pop()
  
  def peek(self):
    return self.container[-1]
  
  def size(self):
    return len(self.container)

# implenting using deque
from collections import deque
class DeStack:
  
  def __init__(self):
    self.container = deque()
    
  def push(self,value):
    self.container.append(value)
    
  def pop(self):
   return self.container.pop()

  def peek(self):
   return self.container[-1]
  
  def size(self):
   return len(self.container)
  
  def items(self):
    return self.container