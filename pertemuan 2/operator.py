# python operators

print(9+8)

#arithmetic operators
sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

x = 15
y = 4

print(x + y)#pertambahan
print(x - y)#pengurangan
print(x * y)#perkalian
print(x / y)#pembagian
print(x % y)#sisa pembagian(modulo)
print(x ** y)#perpangkatan
print(x // y)#pembagian kebawah

#assignment operators
x = 5        
x += 3    
x -= 3
x *= 3
x /= 3
x %= 3
x //= 3
x **= 3
x &= 3
x |= 3
x ^= 3
x >>= 3
x <<= 3

#comparison operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#logical operators
x = 5

print(x > 0 and x < 10)

x = 5

print(x < 5 or x > 10)

x = 5

print(not(x > 3 and x < 10))

#identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#memberships operators
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

#bitwise operators
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#operator presedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)


