print("soal 1")
pasien = [
"Budi Santoso", "Siti Rahayu", "Ahmad Fauzi", "Dewi Lestari",
"Eko Prasetyo", "Fitri Handayani", "Gilang Ramadan", "Hana Pertiwi",
"Irfan Maulana", "Joko Susilo"
]

nama = input("Masukkan nama yang ingin dicari: ")
def linearSearch(arr, targetVal):
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1


result = linearSearch(pasien, nama)

if result != -1:
  print(f"{nama} ditemukan di urutan ke - {result+1}")
else:
  print(f"{nama} tidak ada dalam daftar hari ini")

print()
print("Soal 2")
id_karyawan = [
1021, 1045, 1089, 1102, 1157, 1203, 1245, 1312,
1378, 1401, 1456, 1502, 1567, 1634, 1700
]

id = int(input("Masukkan ID yang ingin dicari: "))
perbandingan = 0

def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    global perbandingan
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      perbandingan+=1
      return mid

    if arr[mid] < targetVal:
      perbandingan+=1
      left = mid + 1
    else:
      right = mid - 1
      perbandingan+=1
    

  return -1


result = binarySearch(id_karyawan, id)

if result != -1:
  print(f"Proses perbandingan: {perbandingan} kali")
  print(f"ID {id} ditemukan! Posisi ke-{result+1} dalam daftar.")
else:
  print(f"{id} tidak terdaftar sebagai karyawan.")

print()
print("soal 3")
rak_a = ["BK-045", "BK-012", "BK-078", "BK-033", "BK-091",
"BK-027", "BK-056"]
rak_b = ["BK-011", "BK-023", "BK-035", "BK-047", "BK-059",
"BK-071", "BK-083", "BK-095"]

kode_buku = input("Masukkan kode buku yang dicari: ")

def linearSearchBuku(arr, targetVal):
  print("Mencari di Rak A (Linear Search)...")
  for i in range(len(arr)):
    if arr[i] == targetVal:
      return i
  return -1

def binarySearch(arr, targetVal):
  print("Mencari di Rak B (Binary Search)...")
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1


result = linearSearchBuku(rak_a, kode_buku)

if result != -1:
  print(f"{kode_buku} ditemukan di Rak A, posisi ke-{result+1}.")
  print(f"Kesimpulan: Buku {kode_buku} tersedia di Rak A.")
else:
  print(f"{kode_buku} tidak ditemukan di Rak A.")
  print()
  result_B = binarySearch(rak_b, kode_buku)
  if result_B != -1:
    print(f"{kode_buku} ditemukan di Rak B, posisi ke-{result_B+1}.")
    print()
    print(f"Kesimpulan: Buku {kode_buku} tersedia di Rak B.")
  else:
    print(f"{kode_buku} tidak ditemukan di Rak B.")
    print(f"Kesimpulan: Buku {kode_buku} tak tersedia.")

#JAWABAN a: KARENA DATA DI RAK A BELUM KE-SORTING JADI GA BISA PAKE BINARY SEARCH
#JAWABAN b: MAKSIMAL LANGKAH MISALNYA RAK B ADA 1000 BUKU, MAKA MAKSIMAL LANGKAH BINARY SEARCH ADALAH LOG2 1000 = 9,97 ATAU DIBULATKAN 10 LANGKAH
#JAWABAN c: MAKSIMAL LANGKAH MISALNYA RAK A ADA 1000 BUKU, MAKA MAKSIMAL LANGKAH LINEAR SEARCH ADALAH SEBANYAK DATA, YAITU 1000 LANGKAH