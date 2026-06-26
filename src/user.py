class User:
    def __init__(self, name, age):
      self.name = name
      self.age = age

    def is_adult(self):
     if (self.age >= 18):
        return True
     else:
       return False
     
    def greet(self):
      print(f"Привет, меня зовут {self.name}, мне {self.age} лет")