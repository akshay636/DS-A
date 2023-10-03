class Employee:
   def __init__(self,first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
   def getFullName(self):
     return '{} {}'.format(self.first, self.last)

em1 = Employee('Akshay', 'Kahjuriya', 100000000000000)
print(em1.getFullName())