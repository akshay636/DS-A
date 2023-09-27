class node:
  def __init__(self, data=None):
    self.data=data
    self.next=None
    
class linked_list:
  
  def __init__(self):
    self.head = node()
    
  def append(self,value):
    new_node = node(value)
    cur = self.head
    while cur.next!=None:
      cur = cur.next
    cur.next = new_node
    
  def display(self):
    cur= self.head
    list =[]
    while cur.next!=None:
      cur = cur.next
      list.append(cur.data)
    return list
      
  def length(self):
    cur = self.head
    len =0
    while cur.next!=None:
      len += 1
      cur = cur.next
    return len
  
  def deleteLast(self):
    cur = self.head
    while cur.next!=None:
      last_node = cur
      cur = cur.next
    last_node.next = cur.next
    return 'Deleted'
  
  def deleteByPos(self, pos):
    if pos > self.length():
      print('error')
      return 'index out of range'
    else:
      cur = self.head
      temPos=1
      while cur.next!=None:
        last_node = cur
        cur = cur.next
        if temPos == pos:
          last_node.next = cur.next
          return
        temPos += 1
  def removeEl(self, el):
    cur= self.head
    while cur.next!=None:
      last_node = cur
      cur = cur.next
      if cur.data ==el:
        last_node.next = cur.next
    return self.display()
          
      
    
ll1=linked_list()
ll1.append(7)
ll1.append(7)
ll1.append(7)
ll1.append(7)
print(ll1.display())
print(ll1.removeEl(7))
