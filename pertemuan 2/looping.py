i = 1
while i < 6:
  print(i)
  i += 1

i = 1
while i < 6:
  print(i)
  if i == 3:
    break#break untuk menghentikan loop lebih cepat saat kondisi terpenuhi
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3:
    continue#untuk me-skip kondisi
  print(i)

#FOR LOOP
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

for x in "banana":
  print(x)

#CONTINUE STATEMENT
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#range() function
for x in range(6):
  print(x)

for x in range(2, 6):
  print(x)

for x in range(2, 30, 3):
  print(x)