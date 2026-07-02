class User:
    """Представляет собой экземпляр пользователя
    
    Атрибуты:
        name (string) - имя пользователя
        age (int) - возраст пользователя

    Методы:
        __init__(self, name, age) - конструктор класса
        is_adult(self) - проверка на совершеннолетие
        greet(self) - приветствие
    """

    def __init__(self, name, age):
      if not isinstance(age, int):
         raise TypeError("Возраст должен быть целым числом")
      self.name = name
      self.age = age

    def is_adult(self):
     return self.age >= 18
     
    def greet(self):
      print(f"Привет, меня зовут {self.name}, мне {self.age} лет")

if __name__ == "__main__":
    man = User("Alex", 40)
    man.greet()