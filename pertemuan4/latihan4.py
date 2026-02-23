# skenario 1: 1. Jalankan kode berikut dan amati outputnya. Coba ubah input yang diberikan
# (angka nol, huruf, angka negatif) dan perhatikan apa yang terjadi.

angka_list = [10, 20, 30]
try:
    idx = int(input('Masukkan index (0-2): '))
    print(f'Nilai: {angka_list[idx]}')
except ValueError:
    print('Harus berupa angka bulat!')
except IndexError:
    print('Index di luar jangkauan!')
finally:
    print('Selesai.')


# skenario 2: Buat program yang meminta 2 angka dari user dan mencetak hasil pembagiannya.
# Tangani semua kemungkinan error yang bisa terjadi.

try:
    print("masukkan angka yang akan dibagi:")
    value  = float(input())
    print("———")
    value2 = float(input())
    print("= ", value/value2)
except ValueError:
    print('input harus angka!')
except ZeroDivisionError:
    print('tidak boleh dibagi 0! Akan membuat hasil tak terdefinisi')