class KendaraanDarat:
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang):
        self.tahun_keluaran = tahun_keluaran
        self.nama = nama
        self.warna = warna
        self.kecepatan = kecepatan
        self.bahan_bakar = bahan_bakar
        self.jumlah_roda = jumlah_roda
        self.kapasitas_penumpang = kapasitas_penumpang

class Kereta(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, gerbong, jumlah_kursi, jenis_layanan_kereta, rute):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.gerbong = gerbong
        self.jumlah_kursi = jumlah_kursi
        self.jenis_layanan_kereta = jenis_layanan_kereta
        self.rute = rute

    def tambah_rute(self, rute_baru):
        self.rute.append(rute_baru)

    def kurangi_rute(self, rute_terhapus):
        if rute_terhapus in self.rute:
            self.rute.remove(rute_terhapus)

class Mobil(KendaraanDarat):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang)
        self.jenis_mobil = jenis_mobil
        self.mesin_hidup = False

    def start_engine(self):
        self.mesin_hidup = True

    def stop_engine(self):
        self.mesin_hidup = False

    def maju(self):
        if self.mesin_hidup:
            print("Mobil bergerak maju.")
        else:
            print("Mesin mati, tidak dapat maju.")

    def mundur(self):
        if self.mesin_hidup:
            print("Mobil bergerak mundur.")
        else:
            print("Mesin mati, tidak dapat mundur.")

    def belok(self, arah):
        if self.mesin_hidup:
            print(f"Mobil belok ke arah {arah}.")
        else:
            print("Mesin mati, tidak dapat belok.")

class MobilBalap(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, front_wing, rear_wing):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.front_wing = front_wing
        self.rear_wing = rear_wing

    def race(self):
        print("Mobil balap sedang berlomba!")

class MobilCrossroad(Mobil):
    def __init__(self, tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil, sunroof_type, shock_breaker):
        super().__init__(tahun_keluaran, nama, warna, kecepatan, bahan_bakar, jumlah_roda, kapasitas_penumpang, jenis_mobil)
        self.sunroof_type = sunroof_type
        self.shock_breaker = shock_breaker

    def sunroof_terbuka(self):
        print("Sunroof terbuka.")

    def sunroof_tertutup(self):
        print("Sunroof tertutup.")

kendaraan_darat = KendaraanDarat(2022, "Kendaraan Darat", "Merah", 0, "Bensin", 4, 5)
rute_kereta = ["Stasiun A", "Stasiun B", "Stasiun C"]
kereta = Kereta(2020, "Kereta Ekspres", "Biru", 100, "Listrik", 16, 200, 5, 150, "Ekonomi", rute_kereta)
mobil = Mobil(2021, "Mobil Sedan", "Hitam", 80, "Bensin", 4, 5, "Sedan")
mobil_balap = MobilBalap(2019, "Balap Mobil", "Merah", 200, "Bensin", 4, 2, "Balap", "Downforce", "Spoiler")
mobil_crossroad = MobilCrossroad(2020, "Off-road Mobil", "Hijau", 60, "Bensin", 4, 4, "Off-road", "Sunroof Kaca", "Suspensi Off-road")

print("Nama Kendaraan Darat:", kendaraan_darat.nama)
print("Warna Kendaraan Darat:", kendaraan_darat.warna)
kereta.tambah_rute("Stasiun D")
print("Rute Kereta:", kereta.rute)
mobil.start_engine()
mobil.maju()
mobil_balap.race()
mobil_crossroad.sunroof_tertutup()

