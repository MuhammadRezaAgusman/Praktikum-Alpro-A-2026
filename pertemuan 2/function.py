#FUNCTION

def my_function(name):
  print("Hello ",name)

my_function("ejaaa")#PEMANGGILAN FUNGSI, jika parameter ada valye maka itu menjadi argument

#function mengembalikan nilai
def get_greeting():
  return "Hello from a function"

message = get_greeting()
print(message)

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)


