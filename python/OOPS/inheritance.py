# inheritance is allow us to get the property and method of another class.
# in simple word a class inherte the methods and variables of another class.

# this is done by the resolution order
# using help function we can see which class is inherited
# syntax print(help(class_name))
# class variable are those variable which is shared amoung  within classes
# isinstance method will tell us if an object is an instance of a class.
# issubclass method will tell us if and class is subclass of another class
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
   
class developer(Employee):
  raise_amount =2
  def __init__(self, first, last, pay, technology):
    super().__init__(first, last, pay)
    self.technology = technology
    
class Manager(Employee):
  def __init__(self, first, last, pay, employees=None):
    super().__init__(first, last, pay)
    self.empolyees = employees
    if self.empolyees is None:
      self.empolyees =[]
    else:
      self.empolyees = employees
  
  def get_employees(self):
    for emp in self.empolyees:
      return emp.first
  
  def add_employe(self,emp):
    if emp not in self.empolyees:
      self.empolyees.append(emp)
      
  def remove_emp(self, emp):
    if emp in self.empolyees:
      self.empolyees.remove(emp)
    
    
   
em1 = Employee('Akshay', 'Kahjuriya', 100000000000000)
emp2 =Employee('Sumit', "khajuriya",100000000000000)
emp2.raise_amount =20

dev1 = developer('Test', 'Manual', 1200, 'selenium')
mangr = Manager('Akshay', 'Khajuriya',100000000000)
mangr.add_employe(dev1)
print(mangr.get_employees())
