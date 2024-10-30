class PersegiPanjang:
    def __init__(self, panjang, lebar):
    #Konstruktor untuk inisialisasi panjang dan lebar
        self.panjang = panjang
        self.lebar = lebar

    def hitung_keliling(self):
    #Fungsi untuk menghitung keliling persegi panjang
        return 2 * (self.panjang + self.lebar)

    def hitung_luas(self):
    #Fungsi untuk menghitung luas persegi panjang
        return self.panjang * self.lebar

    def __str__(self):
    #Fungsi untuk menampilkan string representasi objek
        return f"Persegi Panjang, Panjang: {self.panjang} cm, Lebar: {self.lebar} cm"


if __name__ == "__main__":
    #buat objek persegi panjang
    persegi_panjang = PersegiPanjang(5, 4)

    #nampilkan informasi objek
    print(persegi_panjang)

    #hitung dan menampilkan keliling
    keliling = persegi_panjang.hitung_keliling()
    print(f"Keliling: {keliling} cm")

    #hitung dan menampilkan luas
    luas = persegi_panjang.hitung_luas()
    print(f"Luas: {luas} cm²")