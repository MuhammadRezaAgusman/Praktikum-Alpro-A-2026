a = 33
b = 200
if b > a:
  print("b is greater than a")

number = 15
if number > 0:
  print("The number is positive")

age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

#elif condition
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

#shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")#hanya untuk 1 kondisi saja

a = 2
b = 330
print("A") if a > b else print("B")

#nested if
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#pass statement
a = 33
b = 200

if b > a:
  pass