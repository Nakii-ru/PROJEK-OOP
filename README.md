# PROJEK-OOP

RIDHO FHADLY HAMZAH

312410486

TI.24.A5

# Penjelasan
## Data/Mahasiswa.py

class Mahasiswa:

`__init__`(self, nama, nilai_tugas, nilai_uts, nilai_uas): Konstruktor untuk kelas Mahasiswa, yang menyimpan nama mahasiswa dan nilai tugas, UTS, serta UAS. Konstruktor ini juga menghitung nilai akhir menggunakan metode hitung_nilai_akhir.

`hitung_nilai_akhir(self)`: Fungsi ini menghitung nilai akhir berdasarkan bobot nilai tugas (30%), UTS (35%), dan UAS (35%).

`class DataMahasiswa`:
        
`__init__(self)`: Konstruktor untuk kelas DataMahasiswa yang menginisialisasi daftar mahasiswa kosong (daftar_mahasiswa).
        
`tambah(self, mahasiswa: Mahasiswa)`: Menambahkan objek Mahasiswa ke dalam daftar mahasiswa dan menampilkan pesan konfirmasi.
        
`tampilkan(self)`: Menampilkan daftar mahasiswa beserta nilai tugas, UTS, UAS, dan nilai akhir mereka dalam format tabel.
        
`ubah(self, nama, nilai_tugas, nilai_uts, nilai_uas)`: Mengubah data nilai mahasiswa berdasarkan nama. Jika ditemukan, nilai akan diperbarui, dan nilai akhir akan dihitung ulang.
        
`hapus(self, nama)`: Menghapus data mahasiswa berdasarkan nama. Jika mahasiswa ditemukan, data akan dihapus dari daftar mahasiswa.
```python
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
```
## View/Input_form.py
class InputForm:

input_data(): Fungsi statis yang meminta input dari pengguna untuk nama mahasiswa dan nilai tugas, UTS, serta UAS. Fungsi ini mengembalikan data yang dimasukkan.
```python
# view/input_form.py

class InputForm:
    @staticmethod
    def input_data():
        nama = input("Masukkan nama mahasiswa: ")
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        nilai_uts = float(input("Masukkan nilai UTS: "))
        nilai_uas = float(input("Masukkan nilai UAS: "))
        return nama, nilai_tugas, nilai_uts, nilai_uas
```
 ## View/Mahasiswa.py
   class MahasiswaView:
   __init__(self): Konstruktor yang menginisialisasi objek DataMahasiswa, yang berfungsi untuk menyimpan dan mengelola data mahasiswa.

   tampilkan_daftar(self): Menampilkan daftar mahasiswa dengan memanggil metode tampilkan dari objek DataMahasiswa.

   tambah_mahasiswa(self, mahasiswa): Menambahkan mahasiswa ke dalam daftar dengan memanggil metode tambah dari objek DataMahasiswa.

   ubah_mahasiswa(self, nama, nilai_tugas, nilai_uts, nilai_uas): Mengubah data nilai mahasiswa dengan memanggil metode ubah dari objek DataMahasiswa.

   hapus_mahasiswa(self, nama): Menghapus mahasiswa dari daftar dengan memanggil metode hapus dari objek DataMahasiswa.
```python
from data.mahasiswa import DataMahasiswa

class MahasiswaView:
    def __init__(self):
        self.data_mahasiswa = DataMahasiswa()

    def tampilkan_daftar(self):
        self.data_mahasiswa.tampilkan()

    def tambah_mahasiswa(self, mahasiswa):
        self.data_mahasiswa.tambah(mahasiswa)

    def ubah_mahasiswa(self, nama, nilai_tugas, nilai_uts, nilai_uas):
        self.data_mahasiswa.ubah(nama, nilai_tugas, nilai_uts, nilai_uas)

    def hapus_mahasiswa(self, nama):
        self.data_mahasiswa.hapus(nama)
```
## Main.py

    main(): Fungsi utama yang menyediakan menu untuk pengguna. Menu ini memungkinkan pengguna untuk:
        Menambah mahasiswa dengan memasukkan data nilai.
        Menampilkan daftar mahasiswa yang sudah ada.
        Mengubah nilai mahasiswa.
        Menghapus mahasiswa.
        Keluar dari program.
    Fungsi ini menggunakan objek MahasiswaView untuk berinteraksi dengan data mahasiswa, dan menggunakan InputForm untuk menginput data mahasiswa.
```python
# main.py

from data.mahasiswa import Mahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    view = MahasiswaView()
    
    while True:
        print("\nMenu:")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Daftar Mahasiswa")
        print("3. Ubah Nilai Mahasiswa")
        print("4. Hapus Mahasiswa")
        print("5. Keluar")
        
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            nama, nilai_tugas, nilai_uts, nilai_uas = InputForm.input_data()
            # Create an instance of Mahasiswa instead of MahasiswaView
            mahasiswa = Mahasiswa(nama, nilai_tugas, nilai_uts, nilai_uas)
            view.tambah_mahasiswa(mahasiswa)  # Pass the mahasiswa instance
        
        elif pilihan == "2":
            view.tampilkan_daftar()
        
        elif pilihan == "3":
            nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
            nilai_tugas = float(input("Masukkan nilai tugas baru: "))
            nilai_uts = float(input("Masukkan nilai UTS baru: "))
            nilai_uas = float(input("Masukkan nilai UAS baru: "))
            view.ubah_mahasiswa(nama, nilai_tugas, nilai_uts, nilai_uas)
        
        elif pilihan == "4":
            nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
            view.hapus_mahasiswa(nama)
        
        elif pilihan == "5":
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid")

if __name__ == "__main__":
    main()

```
## Hasil Eksekusi
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-11%20154937.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-11%20155035.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-11%20155115.png?raw=true)
![prak.pict](https://github.com/Nakii-ru/prak.pict/blob/main/Screenshot%202024-12-11%20155126.png?raw=true)
