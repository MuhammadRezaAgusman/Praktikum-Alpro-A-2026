
DAFTAR_ANGKA = [23, 67, 4, 89, 15, 42, 73, 31, 58, 9]
print("=== TEBAK ANGKA GAME ===")
print("tebak angka dengan benar... (0 - 100)")
print()

def tebak_angka(angka_rahasia, maks_percobaan):

    '''meminta input tebakan dari pemain secara berulang menggunakan for loop. Mencetak 
    petunjuk "Terlalu kecil", "Terlalu besar", atau "Benar!" sesuai hasil perbandingan. 
    mengembalikan True jika pemain berhasil menebak, atau False jika percobaan habis
    '''

    global coba
    coba = 7
    for i in range(maks_percobaan):
        try:
            tebakan = int(input("Masukkan Tebakan: "))
        except:
            print("Masukkan angka saja.")
            continue
        if tebakan >= 100 or tebakan <= 0:
            print("angka tebakan hanya dari 0 - 100!")
        if tebakan > angka_rahasia:
            print("Terlalu Besar!")
            coba-=1
        elif tebakan < angka_rahasia:
            print("Terlalu Kecil!")
            coba-=1
        else:
            print("Benar!")
            return True
    return False

def hitung_skor(berhasil, sisa_percobaan):
    """Jika pemain berhasil (berhasil = True), mengembalikan nilai sisa_percobaan*10 
    sebagai skor. Jika tidak berhasil, kembalikan 0.
    """
    if berhasil == True:
        return sisa_percobaan*10
    else:
        return 0

def main_satu_ronde(nama, nomor_ronde):
    """Ambil angka rahasia dari DAFTAR_ANGKA berdasarkan nomor_ronde. 
Jalankan tebak_angka() untuk mendapatkan hasil, kemudian panggil 
hitung_skor() untuk menghitung skor. Kembalikan list [nama, skor]. """
    global skor
    if nomor_ronde>=10:
        DAFTAR_ANGKA.append(nomor_ronde % len(DAFTAR_ANGKA))
    angka_rahasia = DAFTAR_ANGKA[nomor_ronde]
    maks = 10
    menang = tebak_angka(angka_rahasia, maks)
    skor = hitung_skor(menang, coba)
    stats = [nama, skor]
    return stats

def tampilkan_riwayat(riwayat):
    """Cetak seluruh isi list riwayat dalam format tabel yang memuat kolom nomor, 
nama, dan skor. Jika list riwayat kosong, tampilkan pesan: "Belum ada riwayat." """
    copy_riwayat = riwayat.copy()
    if len(copy_riwayat) == 0:
        return 'Belum ada riwayat.'
    else:
        print("Nama| skor")
        for i in range(len(copy_riwayat)):
            print(f"{copy_riwayat[i][0]} | {copy_riwayat[i][1]}")

def selection_sort(riwayat):
    """Buat salinan dari list riwayat, lalu urutkan salinan tersebut dari skor tertinggi ke 
terendah menggunakan algoritma Selection Sort. Data asli (parameter riwayat) 
tidak boleh berubah. Kembalikan salinan yang sudah terurut. """
    copy_riwayat = riwayat.copy()
    n = len(copy_riwayat)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if copy_riwayat[j][1] > copy_riwayat[min_index][1]:
                min_index = j
        copy_riwayat[i], copy_riwayat[min_index] = copy_riwayat[min_index], copy_riwayat[i]
    return copy_riwayat

def tampilkan_leaderboard(riwayat):
    """Panggil selection_sort_riwayat() untuk mendapatkan data yang terurut, kemudian 
cetak hasilnya beserta nomor peringkat. Berikan tanda bintang (*) pada entri 
dengan peringkat pertama."""
    rank = selection_sort(riwayat)
    print("Leaderboard")
    for i in range(len(rank)):
        if i == 0:
            print(f"{i+1}. {rank[i][0]}   {rank[i][1]}*")
        else:
            print(f"{i+1}. {rank[i][0]}   {rank[i][1]}")

riwayat = []
ronde = 0
while True:
    nama = input("Masukkan Nama Anda:")
    print(f"Ronde - {ronde+1} Nama: {nama}")
    riwayat.append(main_satu_ronde(nama, ronde))
    print(f"skor ronde ke - {ronde+1}: {skor}")
    print("apakah anda ingin bermain lagi? ya/tidak")
    keputusan = input().lower()
    if keputusan == 'tidak':
        print()
        break
    elif keputusan == 'ya':
        print("oke lanjut")
        ronde+=1
    print()
  
tampilkan_riwayat(riwayat)
print()
tampilkan_leaderboard(riwayat)