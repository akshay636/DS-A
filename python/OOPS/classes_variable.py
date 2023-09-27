# class variable are those variable which is shared amoung  within classes
class Employee:
   raise_amount = 30
   total_emp =0
   def __init__(self,first, last, pay):
      self.first = first
      self.last = last
      self.pay = pay
      Employee.total_emp += 1
    
   def getFullName(self):
     return '{} {}'.format(self.first, self.last)
   
   def apply_hike(self):
     self.pay = int(self.pay *  self.raise_amount)
     return self.pay
   
em1 = Employee('Akshay', 'Kahjuriya', 100000000000000)
emp2 =Employee('Sumit', "khajuriya",100000000000000)
emp2.raise_amount =20
print(emp2.apply_hike())
print(em1.apply_hike())
print(Employee.total_emp)