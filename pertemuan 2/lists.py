#PYTHON LISTS
#cara buat list:1
thislist = ["apple", "banana", "cherry"]
print(thislist)

#cara kedua
list2 = list(("aku", "orang", "dua"))
print(list2)

#banyak elemen
thislist = ["apple", "banana", "cherry"]
print(len(thislist))

#access list items
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])#negatie indexing

#range of indexes
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#range negative indexes

#check item exist
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

#change list items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#add list item
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)

#remove list item
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)#disini jika ada 2 atau lebih data yang sama, maka yang kehapus hanya yang pertama muncul

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)#fungsi pop() digunakan untuk menghapus item lewat indeks

#jika tak diinput indeks, maka yang dihapus adalah item terakhir
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)