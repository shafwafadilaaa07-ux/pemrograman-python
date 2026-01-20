# program bangun datar 

print("-----PROGRAM PENGHITUNG LUAS DAN KELILING BANGUN DATAR-----")
nama = input("Masukkan Nama Anda: ")
print("Halo", nama)
# menampilkan daftar bangun datar 
print("Dalam program ini, Kita akan menghitung luas dan keliling bangun datar.")
print("Daftar Bangun Datar")
BangunDatar = ["1. persegi panjang", "2. lingkaran", "3. persegi", "4. segitaga"]
print(BangunDatar)

# menggunakan fungsi (def)
def persegi_panjang():
    print("Anda memilih persegi panjang")
    panjang = float(input("Masukkan panjang persegi panjang: "))
    lebar = float(input("Masukkan lebar persegi panjang: "))
    luas = panjang * lebar 
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang", luas)
    print("Keliling Persegi Panjang", keliling)
def lingkaran():
    print("Anda memilih lingkaran")
    jari_jari = float(input("Masukkan jari_jari lingkaran: "))
    luas = 3,14 * jari_jari * jari_jari
    keliling = 2 * 3,14 * jari_jari
    print("Luas Lingkaran", luas)
    print("Keliling Lingkaran", keliling)
def persegi():
    print("Anda memilih persegi")
    sisi = float(input("Masukkan sisi persegi: "))
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi", luas)
    print("Keliling Persegi", keliling)
def segitiga():
    print("Anda memilih segetiga")
    alas = float(input("Masukkan alas segitika: "))
    tinggi = float(input("Masukkan tinggi segitika: "))
    sisi_miring = (alas**2 + tinggi**2)**1/2
    luas = 1/2 * alas * tinggi
    keliling = alas + tinggi + sisi_miring
    print("Luas segitiga", luas)
    print("keliling segitiga", keliling)

# pengguna memilih bangun datar yang akan dihitung luas dan kelilingnya 
pilih = input("Silahkan Pilih Bangun Datar (1-4): ")
if pilih == "1":
    persegi_panjang()
elif pilih == "2":
    lingkaran()
elif pilih == "3":
    persegi()
elif pilih == "4":
    segitiga()
else:
    print("input tidak valid, silahkan pilih bangun datar dari 1-4.")
    
# bertanya ke user mau hitung lagi atau enggak, kalo lagi program akan jalan lagi, kalo enggak, ucapkan terimakasih dengan menggunakan perulangan while
while True:
    hitung_lagi = input("Apakah kita ingin menghitung lagi? (ya atau tidak): ")
    if hitung_lagi == "ya":
        pilih = input("Silahkan Pilih Bangun Datar (1-4): ")
        if pilih == "1":
            persegi_panjang()
        elif pilih == "2":
            lingkaran()
        elif pilih == "3":
            persegi()
        elif pilih == "4":
            segitiga()
        else:
            print("input tidak valid, silahkan pilih bangun datar dari 1-4.")
    elif hitung_lagi == "tidak":
        print(" wokeh, terimakasih telah menggunakan program ini")
        break
    else:
        print("input tidak valid, silahka jawab dengan 'ya' atau 'tidak'.")