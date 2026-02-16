class ClassSaya:
    x = 7

objek1 = ClassSaya()
objek2 = ClassSaya()
objek3 = ClassSaya()
print(objek1.x)
print(objek2.x)
print(objek3.x)

class Anything:
    pass

class Person:
    def __init__(saya, nama, umur = 17):
        saya.nama = nama
        saya.umur = umur
    
    def greet(saya):
        print("helloo, kenalin namaku " + saya.nama)

o1 = Person("Reza", 18)
o2 = Person("Inta")
print(o1.nama, o1.umur)
print(o2.nama, o2.umur)
o1.greet()

class Pesawat:
    def __init__(self, merek, model, produsen):
        self.merek = merek
        self.model = model
        self.produsen = produsen

    def display_info(self):
        return f"{self.merek} {self.model} {self.produsen}"

plane1 = Pesawat("Airbus-A320", "A320", "Airbus")
print(plane1.display_info())

del plane1.merek


class Calculator:
  def add(self, a, b):
    return a + b

  def multiply(self, a, b):
    return a * b

calc = Calculator()
print(calc.add(5, 3))
print(calc.multiply(4, 7))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def celebrate_birthday(self):
    self.age += 1
    print(f"Happy birthday! You are now {self.age}")

p1 = Person("Linus", 25)
p1.celebrate_birthday()
p1.celebrate_birthday()