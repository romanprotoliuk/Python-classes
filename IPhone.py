# python imports 
# from file import function/class/thing
# from file import *
# file.thing
from Phone import Phone

# inheritance in python 
class IPhone(Phone): # like the extends keyword 
  def __init__(self, phone_number, gen, color):
    # Polymorphism 
      super().__init__(phone_number)
      self.gen = gen
      self.color = color
    
  def __str__(self):
      return f'number: {self.phone_number} gen: {self.gen} color: {self.color}'

  def upgrade(self, new_gen):
    """
      takes phone apple store and gets the next gen 
    """
    self.gen = new_gen

my_iphone = IPhone('222-222-2222', '6', 'gold')
print(my_iphone)

jasons_phone = Phone('333-333-3333')
# Polymorphism in action 
my_iphone.text(jasons_phone.phone_number, 'How are you liking the new jitterbug?')
my_iphone.upgrade('7')
print(my_iphone)