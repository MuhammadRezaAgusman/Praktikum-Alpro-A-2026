matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matrix[2][1])

# Matriks 3x3 dengan inisialisasi nilai langsung 
matriks_3x3 = [[1, 2, 3], 
[4, 5, 6], 
[7, 8, 9]] 
# Matriks 2x4 
matriks_2x4 = [[10, 20, 30, 40], 
[50, 60, 70, 80]] 
print('Matriks 3x3:', matriks_3x3) 
print('Matriks 2x4:', matriks_2x4) 
# Output: 
# Matriks 3x3: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] 
# Matriks 2x4: [[10, 20, 30, 40], [50, 60, 70, 80]]

# Matriks 4x4 dengan nilai default 0 
N, M = 4, 4 
matriks_default = [[0 for j in range(M)] for i in range(N)] 
print('Matriks default:', matriks_default) 
# Matriks 3x5 dengan nilai default -1 
matriks_neg = [[-1 for j in range(5)] for i in range(3)] 
print('Matriks -1:', matriks_neg) 

matriks = [[10, 20, 30], 
           [40, 50, 60], 
           [70, 80, 90]] 
 
print(matriks[0][0])  # Output: 10  (baris 0, kolom 0) 
print(matriks[1][2])  # Output: 60  (baris 1, kolom 2) 
print(matriks[2])     # Output: [70, 80, 90]  (seluruh baris 2)

# Iterasi semua elemen 
for i in range(len(matriks)): 
    for j in range(len(matriks[i])): 
        print(f'matriks[{i}][{j}] = {matriks[i][j]}') 

def total_elemen(matriks): 
    total = 0 
    for baris in matriks: 
        for elemen in baris: 
            total += elemen 
    return total 
 
matriks = [[1, 2, 3], 
           [4, 5, 6], 
           [7, 8, 9]] 
 
print('Total manual:', total_elemen(matriks)) 
 
# Cara singkat dengan fungsi bawaan Python 
total_singkat = sum(sum(baris) for baris in matriks) 
print('Total singkat:', total_singkat) 
 
# Output: 
# Total manual: 45 
# Total singkat: 45 


def kali_skalar(matriks, k): 
    hasil = [] 
    for baris in matriks: 
        baris_baru = [elemen * k for elemen in baris] 
        hasil.append(baris_baru) 
    return hasil 
A = [[1, 2, 3], 
     [4, 5, 6]] 
hasil = kali_skalar(A, 3) 
for baris in hasil: 
    print(baris) 
# Output: 
# [3, 6, 9] 
# [12, 15, 18]

