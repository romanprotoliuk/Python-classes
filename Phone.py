class Phone: 
  """
    a phone that can call and text 
  """
  def __init__(self, phone_number):
    self.phone_number = phone_number

  def __str__(self):
    return f'{self.phone_number}'
  
  def call(self, other_number):
    """
      make a call to another phone 
    """
    print(f'calling {other_number} from {self.phone_number}')
  
  def text(self, other_number, msg):
    """
      text another phone 
    """
    print(f'sending message to {other_number} from {self.phone_number}')
    print(msg)

if __name__ == '__main__':
  my_phone = Phone('555-555-5555')
  print(my_phone)
  my_phone.call('666-643-6321')
  my_phone.text('654-123-1234', 'Not today Roman!')