from collections import deque
class Queue:
  def __init__(self):
    self.line = deque()
    
  def enque(self, value):
    self.line.append(value)
    
  def deque(self):
    self.line.popleft()
    
  def size(self):
    return len(self.line)
  
  def isEmpty(self):
    return len(self.line)==0
  
queue = Queue()
queue.enque(10)
# queue.enque(20)
# queue.enque(30)
# queue.enque(40)
queue.deque()
print(queue.isEmpty())
