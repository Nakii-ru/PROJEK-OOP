class Mahasiswa:
    def __init__(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.nama = nama
        self.nilai_tugas = nilai_tugas
        self.nilai_uts = nilai_uts
        self.nilai_uas = nilai_uas
        self.nilai_akhir = self.hitung_nilai_akhir()

    def hitung_nilai_akhir(self):
        return (self.nilai_tugas * 0.3) + (self.nilai_uts * 0.35) + (self.nilai_uas * 0.35)

class DataMahasiswa:
    def __init__(self):
        self.daftar_mahasiswa = []

    def tambah(self, mahasiswa: Mahasiswa):
        self.daftar_mahasiswa.append(mahasiswa)
        print(f"Data mahasiswa {mahasiswa.nama} telah ditambahkan.")

    def tampilkan(self):
        if not self.daftar_mahasiswa:
            print("Daftar mahasiswa kosong.")
            return
        print("=" * 56)
        print("   |               Daftar Nilai Mahasiswa              |")
        print("=" * 56)
        print("No | Nama       | Tugas | UTS   | UAS   | Nilai Akhir  |")
        print("=" * 56)
        for i, mhs in enumerate(self.daftar_mahasiswa, start=1):
            print(f"{i:2} | {mhs.nama:<10} | {mhs.nilai_tugas:5.1f} | {mhs.nilai_uts:5.1f} | {mhs.nilai_uas:5.1f} | {mhs.nilai_akhir:5.1f}        |")
        print("=" * 56)

    def ubah(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        for mhs in self.daftar_mahasiswa:
            if mhs.nama == nama:
                mhs.nilai_tugas = nilai_tugas
                mhs.nilai_uts = nilai_uts
                mhs.nilai_uas = nilai_uas
                mhs.nilai_akhir = mhs.hitung_nilai_akhir()
                print(f"Data mahasiswa {nama} telah berhasil diubah.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")

    def hapus(self, nama):
        for mhs in self.daftar_mahasiswa:
            if mhs.nama == nama:
                self.daftar_mahasiswa.remove(mhs)
                print(f"Data mahasiswa {nama} telah dihapus.")
                return
        print(f"Mahasiswa dengan nama {nama} tidak ditemukan.")
