class grandFather:
  blood_type = 'o+'
  surname = 'Khajuriya'
  def __init__(self, name):
    self.name = name
  def bold(self):
    return self.blood_type
  
  def details(self):
    return '{} {}'.format(self.name,self.surname)
  
class parent(grandFather):
  colour ='Brown'
  def __init__(self, Fname):
    super().__init__(self)
    self.name = Fname
  
  def details(self):
    self.colour = self.colour
    return super().details()
    
class child(parent):
  def __init__(self, Fname):
    super().__init__(Fname)
    self.name = Fname
  
  
g = grandFather("Kanhaiya")
p = parent('Shyamlal')
son = child('AKshay')
print(g.details())
print(son.details())