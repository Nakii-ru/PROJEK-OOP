# view/mahasiswa.py

class MahasiswaView:
    @staticmethod
    def tampilkan_list(data):
        if not data:
            print("Daftar mahasiswa kosong.")
            return
        
        print("=" * 56)
        print("   |               Daftar Nilai Mahasiswa              |")
        print("=" * 56)
        print("No | Nama       | Tugas | UTS   | UAS   | Nilai Akhir  |")
        print("=" * 56)

        for i, mhs in enumerate(data, start=1):
            print(f"{i:2} | {mhs.nama:<10} | {mhs.nilai_tugas:5.1f} | {mhs.nilai_uts:5.1f} | {mhs.nilai_uas:5.1f} | {mhs.nilai_akhir:5.1f}        |")
        
        print("=" * 56)
