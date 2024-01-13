class Penyakit:
    def __init__(self, nama_penyakit, jenis_penyakit):
        self._nama_penyakit = nama_penyakit
        self._jenis_penyakit = jenis_penyakit

    def tampilkan_info(self):
        print(f"Informasi Penyakit: {self._nama_penyakit}")
        print(f"Jenis Penyakit: {self._jenis_penyakit}")

    def diagnosa(self):
        return f"Diagnosa untuk {self._nama_penyakit}"

class PenyakitKulit(Penyakit):
    def __init__(self, nama_penyakit):
        super().__init__(nama_penyakit, "Kulit")

    def diagnosis_kulit(self):
        return f"Diagnosa khusus kulit untuk {self._nama_penyakit}"

class PenyakitDalam(Penyakit):
    def __init__(self, nama_penyakit):
        super().__init__(nama_penyakit, "Dalam")

    def diagnosis_dalam(self):
        return f"Diagnosa khusus dalam untuk {self._nama_penyakit}"

class PenyakitRingan(Penyakit):
    def __init__(self, nama_penyakit):
        super().__init__(nama_penyakit, "Ringan")

class PemeriksaanPenyakit(PenyakitDalam):
    def __init__(self, nama_penyakit):
        super().__init__(nama_penyakit)
        self._jenis_pemeriksaan = "Pemeriksaan Umum"

    def tampilkan_info_pemeriksaan(self):
        print(f"Informasi Pemeriksaan Penyakit: {self._nama_penyakit}")
        print(f"Jenis Pemeriksaan: {self._jenis_pemeriksaan}")

    def resep_obat(self):
        return f"Resep obat untuk {self._nama_penyakit}"

class Penanganan:
    def __init__(self):
        self._alternatif_penanganan = {}

    def tampilkan_alternatif_penanganan(self):
        print("Alternatif Penanganan:")
        for penyakit, penanganan in self._alternatif_penanganan.items():
            print(f"{penyakit}: {penanganan}")

    def tambah_alternatif_penanganan(self, penyakit, penanganan):
        self._alternatif_penanganan[penyakit] = penanganan

class Obat:
    def __init__(self, nama_obat, fungsi, harga, dosis, efek_samping):
        self._nama_obat = nama_obat
        self._fungsi = fungsi
        self._harga = harga
        self._dosis = dosis
        self._efek_samping = efek_samping

    def tampilkan_info(self):
        print(f"Informasi Obat: {self._nama_obat}")
        print(f"Fungsi: {self._fungsi}")
        print(f"Harga: {self._harga}")
        print(f"Dosis: {self._dosis}")
        print(f"Efek Samping: {self._efek_samping}")

class ObatBerbahaya(Obat):
    def tampilkan_info(self):
        super().tampilkan_info()
        print("Perhatian: Obat ini termasuk obat berbahaya!")

class ObatUmum(Obat):
    pass

class User:
    def __init__(self):
        self._nama = ""
        self._status_login = False
        self._list_obat = []

    def login(self):
        self._status_login = True

    def logout(self):
        self._status_login = False

    def input_info_user(self):
        self._nama = input("Masukkan nama Anda: ")

    def input_info_penyakit(self):
        nama_penyakit = input("Masukkan nama penyakit: ")
        jenis_penyakit = input("Masukkan jenis penyakit (Kulit/Dalam/Ringan): ")

        if jenis_penyakit.lower() == "kulit":
            return PenyakitKulit(nama_penyakit)
        elif jenis_penyakit.lower() == "dalam":
            return PenyakitDalam(nama_penyakit)
        elif jenis_penyakit.lower() == "ringan":
            return PenyakitRingan(nama_penyakit)
        else:
            print("Jenis penyakit tidak valid.")
            return None

    def input_info_obat(self):
        nama_obat = input("Masukkan nama obat: ")
        fungsi = input("Masukkan fungsi obat: ")
        harga = float(input("Masukkan harga obat: "))
        dosis = input("Masukkan dosis obat: ")
        efek_samping = input("Masukkan efek samping obat: ")

        jenis_obat = input("Masukkan jenis obat (Berbahaya/Umum): ")

        if jenis_obat.lower() == "berbahaya":
            return ObatBerbahaya(nama_obat, fungsi, harga, dosis, efek_samping)
        elif jenis_obat.lower() == "umum":
            return ObatUmum(nama_obat, fungsi, harga, dosis, efek_samping)
        else:
            print("Jenis obat tidak valid.")
            return None

    def menu_beli_obat(self):
        while True:
            if not self._status_login:
                print("Anda harus login terlebih dahulu.")
                return

            print("Menu Beli Obat:")

            for i, obat in enumerate(self._list_obat, 1):
                if isinstance(obat, Obat):
                    print(f"{i}. {obat._nama_obat} - {obat._harga} IDR")
                elif isinstance(obat, Penyakit):
                    print(f"{i}. {obat._nama_penyakit} - Penanganan")
                else:
                    print(f"{i}. Tipe objek tidak valid")

            nomor_obat = int(input("Pilih nomor obat (0 untuk keluar): "))
            
            if nomor_obat == 0:
                break

            obat_terpilih = self._list_obat[nomor_obat - 1]
            if isinstance(obat_terpilih, Obat):
                obat_terpilih.tampilkan_info()

                if isinstance(obat_terpilih, ObatBerbahaya):
                    print("Maaf, Anda tidak dapat membeli obat berbahaya.")
                    continue

                jumlah_pembelian = int(input("Masukkan jumlah pembelian: "))

                print("Resi Pembelian:")
                print(f"Nama: {self._nama}")
                print(f"Obat: {obat_terpilih._nama_obat}")
                print(f"Jumlah Pembelian: {jumlah_pembelian}")
                print(f"Total Harga: {jumlah_pembelian * obat_terpilih._harga} IDR")
            else:
                print("Ini bukan obat yang bisa dibeli.")

    def menu_konsultasi(self):
        while True:
            if not self._status_login:
                print("Anda harus login terlebih dahulu.")
                return

            print("Menu Konsultasi:")
            gejala = input("Masukkan gejala yang Anda rasakan (0 untuk keluar): ")

            if gejala == "0":
                break

            print("Rekomendasi Obat dan Diagnosis:")
            for obat in self._list_obat:
                if isinstance(obat, Penyakit):
                    obat.tampilkan_info()
                    print(obat.diagnosa())
                print()

user1 = User()
user1.input_info_user()

user1._list_obat.append(user1.input_info_penyakit())
user1._list_obat.append(user1.input_info_obat())

user1.login()

user1.menu_konsultasi()
user1.menu_beli_obat()
