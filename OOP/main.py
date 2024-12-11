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
