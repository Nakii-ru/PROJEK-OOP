# view/input_form.py

class InputForm:
    @staticmethod
    def input_data():
        nama = input("Masukkan nama mahasiswa: ")
        nilai_tugas = float(input("Masukkan nilai tugas: "))
        nilai_uts = float(input("Masukkan nilai UTS: "))
        nilai_uas = float(input("Masukkan nilai UAS: "))
        return nama, nilai_tugas, nilai_uts, nilai_uas
