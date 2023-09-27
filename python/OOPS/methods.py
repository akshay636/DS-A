class Home:
  bill=150
  member=6
  is_on= False
  def on_bulb(self,action):
    self.is_on = action
    if(action):
      self.is_on = False
    else:
      self.is_on = True
    return self.is_on
  
  def count_member(self):
    return self.member
  
  @classmethod
  def raise_bill(cls, amount):
    cls.bill += amount
    return
  
  @staticmethod
  def is_vacation(day):
    print(day.weekday())
    if day.weekday() ==5 or day.weekday()==6:
      return True
    return False

h1 = Home()
# print(h1.bill)
# print(h1.count_member())
# print(h1.on_bulb(True))
# print(h1.raise_bill(30))
# print(h1.bill)
import datetime
date = datetime.date(23,9,24)
print(Home.is_vacation(date))