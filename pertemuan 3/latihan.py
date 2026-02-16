class  Pesawat:
    def __init__(plane, maskapai, jenis, produksi):
        plane.maskapai = maskapai
        plane.jenis = jenis
        plane.produksi = produksi
    
    def tombol_roda_on(plane):
        print("roda keluar")
    
    def tombol_roda_off(plane):
        print("roda masuk")
    
    def setir_kanan(plane):
        print("belok kanan")
    
    def setir_kiri(plane):
        print("belok kiri")

pesawat1 = Pesawat("garuda indonesia", "B737", "BOEING")
pesawat2 = Pesawat("Lion Air", "Airbus A320", "Airbus")

pesawat1.maskapai = "Qantas"

print(pesawat1.maskapai, pesawat1.jenis)