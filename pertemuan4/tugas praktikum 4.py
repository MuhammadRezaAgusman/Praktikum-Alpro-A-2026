"""Bagian custom exception"""
class NamaError(Exception):# membuat class parent untuk exception nama
    def __init__(self, nama, pesan):
        self.nama = nama
        super().__init__(pesan)

class NamaTerlaluPendek(NamaError):# child class ini untuk error validasi panjang karakter valid
    def __init__(self, nama):
        super().__init__(nama, " Nama terlalu pendek! Minimal 3 karakter.")

class NamaHarusAlphabet(NamaError):# child class ini untuk error nama yang mengandung angka
    def __init__(self, nama):
        super().__init__(nama," Nama harus hanya mengandung alphabet!")


class UmurError(Exception):#exception untuk data umur
    def __init__(self,umur, pesan):
        self.umur = umur
        super().__init__(pesan)

class UmurInvalid(UmurError):# umur tak valid jika mengandung karakter selain angka
    def __init__(self, umur):
        super().__init__(umur," Umur hanya mengandung angka!")

class UmurIlegal(UmurError):# umur ilegal jika melewati rentang syarat daftar
    def __init__(self, umur):
        super().__init__(umur," Umur tidak memenuhi syarat (17-60 tahun).")


class EmailError(Exception):# exception untuk data email
    def __init__(self, email, pesan):
        self.email = email
        super().__init__(pesan)

class EmailWhiteSpace(EmailError):#email tidak boleh ada spasi
    def __init__(self, email):
        super().__init__(email, " Email tidak boleh mengandung spasi")

class EmailInvalid(EmailError):# email invalid jika tak mengandung '@'
    def __init__(self, email):
        super().__init__(email, " Email tidak valid! harus mengandung '@'. ")

class EmailMultiAt(EmailError):# email juga invalid jika mengandung lebih dari satu '@'
    def __init__(self, email):
        super().__init__(email, "Email hanya mengandung satu'@'.")


class NomorTeleponError(Exception):# exception untuk nomor telepon
    def __init__(self, nomor, pesan):
        self.nomor = nomor
        super().__init__(pesan)

# nomor telepon invalid jika mengandung karakter selain angka
class NomorTeleponTypeError(NomorTeleponError):
    def __init__(self, nomor):
        super().__init__(nomor, " Nomor telepon hanya boleh mengandung angka.")

class NomorTeleponInvalid(NomorTeleponError):# nomor hanya boleh 10 -13 digit
    def __init__(self, nomor):
        super().__init__(nomor, " Nomor harus mengandung 10 -13 digit angka.")

"""bagian fungsi validasi"""
def validasi_nama(nama_input):# fungsi validasi nama
    if len(nama_input) < 3:
            raise NamaTerlaluPendek(nama_input)
    if any(c.isdigit() for c in nama_input):
            raise NamaHarusAlphabet(nama_input)
    
def validasi_umur(usia_input):# fungsi validasi umur
    if not usia_input.isdigit():
        raise UmurInvalid(usia_input)
    umur = int(usia_input)
    if umur < 17 or umur > 60:
        raise UmurIlegal(umur)

def validasi_email(email_input):# fungsi validasi email
    if email_input.count("@") == 0:
        raise EmailInvalid(email_input)
    if email_input.count("@") > 1:
        raise EmailMultiAt(email_input)
    if ' ' in email_input:
        raise EmailWhiteSpace(email_input)

def validasi_nomor_telepon(nomor_input):# fungsi validasi nomor telepon
    if not nomor_input.isdigit():
        raise NomorTeleponTypeError(nomor_input)
    if len(nomor_input) < 10 or len(nomor_input) > 13:
        raise NomorTeleponInvalid(nomor_input)
    
"""Bagian proses input dan try-except"""
print("=== REGISTRASI PESERTA SEMINAR ===")
while True:# blok input nama
    try:
        nama = input("Nama Lengkap : ")
        nama_valid = validasi_nama(nama)
    except NamaError as ne:
        print(f"  [ERROR] {ne}")
    else:
        break

while True:# blok input umur
    try:
        usia = input("Usia         : ")
        usia_valid = validasi_umur(usia)
    except UmurError as ue:
        print(f"  [ERROR] {ue}")
    else:
        break

while True:# blok input email
    try:
        email = input("Email        : ")
        email_valid = validasi_email(email)
    except EmailError as ee:
        print(f"  [ERROR] {ee}")
    else:
        break

while True:# blok input nomor telepon
    try:
        nomorTelepon = input("Nomor Telepon: ")
        nomor_valid = validasi_nomor_telepon(nomorTelepon)
    except NomorTeleponError as nte:
        print(f"  [ERROR] {nte}")
    else:
        try: pass
        finally:
           print("Proses input selesai.\n")
        break

"""Jika data yang dimasukkan telah benar semua, maka
sistem akan menampilkan data yang telah diisi user kembali
dan menampilkan status registrasi user"""
print(f"""=== DATA PESERTA ===
Nama   : {nama}
Umur   : {usia}
Email  : {email}
No HP  : {nomorTelepon}
Status : TERDAFTAR""")