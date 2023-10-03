class Parent:
  surname ='Khajuriya'
  father_name =''
  def __init__(self, name):
    self.father_name = name
  def fullName(self, name):
    return '{} {} {}'.format(name, self.father_name, self.surname)
    
class Child1(Parent):
  def __init__(self, name):
    super().__init__(name)
  
  def fullName(self, name='John'):
      return '{} Jr. {} {}'.format(name, self.father_name, self.surname)

    
class Child2(Parent):
  def __init__(self, name):
    super().__init__(name)
    
parent = Parent('Shyanlal')
son1 = Child1("Shyamlal")
son2 = Child2('Shyamlal')

print(son1.fullName("Sumit"))
print(son2.fullName("Akshay"))