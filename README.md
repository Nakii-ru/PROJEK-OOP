# PROJEK-OOP

RIDHO FHADLY HAMZAH

312410486

TI.24.A5

# Penjelasan
1. data/mahasiswa.py

    class Mahasiswa:
        __init__(self, nama, nilai_tugas, nilai_uts, nilai_uas): Konstruktor untuk kelas Mahasiswa, yang menyimpan nama mahasiswa dan nilai tugas, UTS, serta UAS. Konstruktor ini juga menghitung nilai akhir menggunakan metode hitung_nilai_akhir.
        hitung_nilai_akhir(self): Fungsi ini menghitung nilai akhir berdasarkan bobot nilai tugas (30%), UTS (35%), dan UAS (35%).

    class DataMahasiswa:
        __init__(self): Konstruktor untuk kelas DataMahasiswa yang menginisialisasi daftar mahasiswa kosong (daftar_mahasiswa).
        tambah(self, mahasiswa: Mahasiswa): Menambahkan objek Mahasiswa ke dalam daftar mahasiswa dan menampilkan pesan konfirmasi.
        tampilkan(self): Menampilkan daftar mahasiswa beserta nilai tugas, UTS, UAS, dan nilai akhir mereka dalam format tabel.
        ubah(self, nama, nilai_tugas, nilai_uts, nilai_uas): Mengubah data nilai mahasiswa berdasarkan nama. Jika ditemukan, nilai akan diperbarui, dan nilai akhir akan dihitung ulang.
        hapus(self, nama): Menghapus data mahasiswa berdasarkan nama. Jika mahasiswa ditemukan, data akan dihapus dari daftar mahasiswa.

2. view/input_form.py

    class InputForm:
        input_data(): Fungsi statis yang meminta input dari pengguna untuk nama mahasiswa dan nilai tugas, UTS, serta UAS. Fungsi ini mengembalikan data yang dimasukkan.

3. view/mahasiswa.py

    class MahasiswaView:
        __init__(self): Konstruktor yang menginisialisasi objek DataMahasiswa, yang berfungsi untuk menyimpan dan mengelola data mahasiswa.
        tampilkan_daftar(self): Menampilkan daftar mahasiswa dengan memanggil metode tampilkan dari objek DataMahasiswa.
        tambah_mahasiswa(self, mahasiswa): Menambahkan mahasiswa ke dalam daftar dengan memanggil metode tambah dari objek DataMahasiswa.
        ubah_mahasiswa(self, nama, nilai_tugas, nilai_uts, nilai_uas): Mengubah data nilai mahasiswa dengan memanggil metode ubah dari objek DataMahasiswa.
        hapus_mahasiswa(self, nama): Menghapus mahasiswa dari daftar dengan memanggil metode hapus dari objek DataMahasiswa.

4. main.py

    main(): Fungsi utama yang menyediakan menu untuk pengguna. Menu ini memungkinkan pengguna untuk:
        Menambah mahasiswa dengan memasukkan data nilai.
        Menampilkan daftar mahasiswa yang sudah ada.
        Mengubah nilai mahasiswa.
        Menghapus mahasiswa.
        Keluar dari program.
    Fungsi ini menggunakan objek MahasiswaView untuk berinteraksi dengan data mahasiswa, dan menggunakan InputForm untuk menginput data mahasiswa.
