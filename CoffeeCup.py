# important Object Oriented Programming Words 
# Abstraction -- turn code into an object factory 
def make_cup():
  # Encapsulation -- grouping data and methods that manipulate the data together
  this = {}
  this['capacity'] = 10
  this['amount'] = 0

  def drink(this):
    this['amount'] = this['amount'] - 2

  this['drink' ] = drink

  return this 

# abstraction allows us to make many coffee cups 
# red_cup = make_cup()
# print(red_cup)
# blue_cup = make_cup()

# Inheritance -- all the props and methods of a class can be given to a child class
def teac_cup():
  # inheritance -- props and methods from parent 
  this = make_cup()
  this['tea_type'] = 'greens'
  # ...tea methods 

my_tea = teac_cup()

# Polymorphism -- all of the parents properties and methods will work perfectly with the child class 
my_tea['drink']()


# Our digital coffee cup 
# capacity -- how much the cup can hold 
# amount -- current amount of coffee 

capacity = 10 
amount = 0


# we will be able to file the cup with coffee 
# drink from the cup 
# empty the cup to dump out the coffee 

def drink():
  amount - 2

# ...



# create a class with the class keyword -- PascalCase the name 
class CoffeCup():
  # class constructor 
  # method method override on the __init__ (ref to instance (self), ...props) method 
  def __init__(self, capacity):
    self.capacity = capacity

  def __str__(self):
    # what ever string we return will be shown when an instance is printed 
    return f'capacity: {self.capacity} amount: {self.amount}'

  # Intance methods
  def fill(self):
    # cup is always filled to the brim 
    self.amount = self.capacity

  def drink(self, drink_size): 
    # remove amount 
    self.amount -= drink_size
    # if self.amount < 0:
    #   self.amount = 0
    # [value is true] if [condition] else [value if false]
    self.amount = 0 if self.amount < 0 else self.amount 

# making an instance of the class 
jasons_cup = CoffeCup(15)
westons_cup = CoffeCup(10)


jasons_cup.fill()
jasons_cup.drink(10)
print(jasons_cup)