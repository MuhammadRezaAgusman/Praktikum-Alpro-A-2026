struktur = {
    "Skripsi_Aqil": {
        "Bab_1": {
            "pendahuluan.docx": 45,
            "latar_belakang.docx": 62
        },
        "Bab_2": {
            "landasan_teori.docx": 118,
            "referensi": {
                "paper_A.pdf": 340,
                "paper_B.pdf": 210
                }
        },
        "Bab_3": {
            "metodologi.docx": 89,
            "diagram": {
                "flowchart.png": 512,
                "erd.png": 278,
                "arsitektur": {
                    "sistem.png": 430
                }
            }
        },
        "sidang": {
            "presentasi.pptx": 2048,
            "catatan_revisi.txt": 15
        },
        "README.txt": 8
    }
}

def total_ukuran(folder: dict) -> int:
    total = 0

    for v in folder.values():
        if isinstance(v, dict):
            total += total_ukuran(v)
        elif isinstance(v, int):
            total += v

    return total
print("Total ukuran skripsi: ", total_ukuran(struktur), "KB")

def hitung_file(folder:dict) -> int:
    hitung = 0
    for v in folder.values():
        if isinstance(v, dict):
            hitung += hitung_file(v)
        elif isinstance(v, int):
            hitung+=1
    return hitung
print(f"Jumlah File: {hitung_file(struktur)} file")

def cari_terbesar(folder: dict) -> tuple:
    nama_file = None
    ukuran_kb = -1

    for nama, v in folder.items():
        if isinstance(v, dict):
            sub_nama, sub_ukuran = cari_terbesar(v)
            if sub_ukuran > ukuran_kb:
                nama_file = sub_nama
                ukuran_kb = sub_ukuran

        elif isinstance(v, int):
            if v > ukuran_kb:
                nama_file = nama
                ukuran_kb = v

    return (nama_file, ukuran_kb)

print(f"File Terbesar: {cari_terbesar(struktur)[0]} ({cari_terbesar(struktur)[1]} KB)")

def tampilkan_tree(folder: dict, nama: str = "", level: int = 0):
    indent = "  " * level
    print(f"{indent}{nama}/")

    for k, v in folder.items():
        if isinstance(v, dict):
            tampilkan_tree(v, k, level + 1)
        else:
            print(f"{'  ' * (level + 1)}{k} ({v} KB)")
tampilkan_tree(struktur)