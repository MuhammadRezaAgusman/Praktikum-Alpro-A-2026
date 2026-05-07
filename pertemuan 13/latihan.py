import os
while True:

    print("""============================
PYTHON FILE MANAGER v1.0
============================
[1] Read file
[2] Write file
[3] Delete file
[0] Exit
------------------------------""")

    user = int(input("Pilih Menu: "))

    if user == 1:
        print("File Tersedia: ")
        data_file = [f for f in os.listdir("C:\latihan coding\Praktikum-Alpro-A-2026\pertemuan 13") if f.endswith(".txt")] 
        for i in range(len(data_file)):
            print(f'[{i+1}] {data_file[i]}')
        file = int(input('Pilih file(nomor): '))
        with open(data_file[file-1]) as t:
                print(f"--- Isi {data_file[file-1]} ---")
                print(t.read())
                print("----------------------")        
    
            
    elif user == 2:
        print("File Tersedia: ")
        data_file = [f for f in os.listdir("C:\latihan coding\Praktikum-Alpro-A-2026\pertemuan 13") if f.endswith(".txt")] 
        for i in range(len(data_file)):
            print(f'[{i+1}] {data_file[i]}')
        pilihan = int(input('Pilih file(nomor): '))
        with open(data_file[pilihan-1], 'a') as t:
                print(f"--- Isi {data_file[pilihan-1]} ---")
                chamber = input("")
                t.write(chamber)
                print("----------------------") 
        
    elif user == 3:
        print("File Tersedia: ")
        data_file = [f for f in os.listdir("C:\latihan coding\Praktikum-Alpro-A-2026\pertemuan 13") if f.endswith(".txt")] 
        for i in range(len(data_file)):
            print(f'[{i+1}] {data_file[i]}')
        pilihan = input("Pilihan (Nama file): ")
        if os.path.exists(pilihan):
            os.remove(pilihan)
            print("File Telah Terhapus")
        else:
            print("File Tidak Ada")
    elif user == 0:
        break
    else:
         print('Pilihan Salah!')
        