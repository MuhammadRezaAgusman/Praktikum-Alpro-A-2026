A = [[5, 3, 1],
     [2, 8, 4],
     [6, 0, 7]]
B = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

#a) Menjumlahkan matriks A dan B, simpan hasilnya dalam variabel C_tambah

def plus_matrix(mtx_A, mtx_B):
    if len(mtx_A) != len(mtx_B) or len(mtx_A[0]) != len(mtx_B[0]):
        print("Error! ukuran matriks tak sama.")
    baris, kolom = len(mtx_A), len(mtx_A[0])
    sum = [[mtx_A[i][j]+mtx_B[i][j] for j in range(kolom)] for i in range(baris)]
    return sum
C_tambah = plus_matrix(A, B)

#b) Mengurangkan matriks A dikurangi B, simpan dalam variabel C_kurang
def minus_matrix(mtx_A, mtx_B):
    if len(mtx_A) != len(mtx_B) or len(mtx_A[0]) != len(mtx_B[0]):
        print("Error! ukuran matriks tak sama.")
    baris, kolom = len(mtx_A), len(mtx_A[0])
    sum_min = [[mtx_A[i][j]-mtx_B[i][j] for j in range(kolom)] for i in range(baris)]
    return sum_min
C_kurang = minus_matrix(A, B)

#c) Mengalikan setiap elemen matriks A dengan skalar k = 4 , simpan dalam C_skalar
def kali_skalar(matriks, k): 
    hasil = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        hasil.append(baris_baru) 
    return hasil 
C_skalar = kali_skalar(A, 4)

#D) Menampilkan ketiga hasil dengan format rapi baris per baris
print("C_tambah=")
for baris in C_tambah: 
    print(baris)

print("C_kurang=")
for baris in C_kurang: 
    print(baris)

print("C_skalar=")
for baris in C_skalar: 
    print(baris)