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