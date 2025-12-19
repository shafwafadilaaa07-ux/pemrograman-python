print("---latihan list (daftar)---")
#lists adalah tipe data di python yang digunakan untuk menyimpan banyak data dalam satu variabel
#python lists menggunakan kurung siku []


lagu = ["young and beautiful", "like we just met", "lovely"]
    #            0                      1              2
print(lagu)
print(lagu[1]) #menggunakan Index, index dimulai dari 0
print(lagu[-3]) #Pengindeksan negatif berarti mulai dari akhir. -1mengacu pada item terakhir, -2mengacu pada item kedua terakhir, dan seterusnya.

print("---latihan mengubah item di list")
sayur = ["kol", "wortel", "sawi", "kentang", "cabe"]
sayur[4] = "brokoli"
print(sayur)

print("---latihan untuk menambah item di list---")
#untuk menambahkan item ke akhir daftar, gunakan append
lagu = ["young and beautiful", "like we just met", "lovely"]
lagu.append("chanel")
print(lagu)
lagu.insert(2, "big boy") #untuk menambahkan item dan menentukan indexnya
print(lagu)

print("---latihan untuk menghapus item di list---")
#untuk menghapus item tertentu, gunakan remove
kpop = ["nct", "enhypen", "aespa", "babymonster", "straykids"]
kpop.remove("aespa")
print(kpop)
#untuk menghapus index yang ditentukan, gunakan pop()
kpop = ["nct", "enhypen", "aespa", "babymonster", "straykids"]
kpop.pop(4)
print(kpop)

print("---latihan perulangan---")
#perulangan menggunakan for
#for digunakan untuk mencetak perulangan daftar, satu per satu
#latihan daftar pengulangan lists melalui daftar
nama = ["jeno", "choihyunwok", "jungwoon", "lee dongwook", "bright"]
for x in nama:
    print(x)
    
#LATIHAN PERULANGAN MELALUI NOMER INDEXNYA
#untuk melakukan perulangan melalui nomer index Gunakan fungsi ` range()and` len()untuk membuat objek dapat berubah..
nama = ["jeno", "shafwa", "mark", "jay", "jake"]
for s in range(len(nama)):
    print(nama[s])
    
#perulangan menggunakan while
#while digunakan untuk menulusuri semua nomer index.
nama = ["jeno", "shafwa", "choihyunwook"]
j = 0
while j < len (nama):
    print(nama[j])
    j = j + 1
    
print("---pemahaman list---")
#list comprehension menggunakan sintaks yang lebih singkat ketika kita ingin membuat daftar baru berdasarkan item dari lists yang sudah ada
#berdasarkan kpop yang ada di atasa kita menginginkan lists baru yang namanya mengandung huruf a 
#tanpa list conprehension, kita harus menulis for pernyataan dengan uji kondisional di dalamnya
kpop = ["nct", "enhypen", "aespa", "babymonster", "straykids"]
newlist = []
for j in kpop:
    if "a" in j:
        newlist.append(j)
print(newlist)
#atau kita bisa melakukannya dengan satu baris kode
kpop = ["nct", "enhypen", "aespa", "babymonster", "straykids"]
newlist = [j for j in kpop if "a" in j]
print(newlist)

print("--latihan urutan dalam list---")
#Objek List memiliki sort()metode yang akan mengurutkan daftar secara alfanumerik(kombinasi huruf dan angka), menaik, secara default(penganturan bawaan)
#Urutan Daftar Secara alfebetis
#list alfebetis adalah daftar yang diurutkan dari yang terkecil ke terbesar misal dari (A-Z)
nama = ["jeno", "shafwa", "choihyunwook", "jungwoon"]
nama.sort()
print(nama)
#Urutan Daftar Secara Numerik
angka = [23, 25, 19, 27, 20]
angka.sort()
print(angka)

#Urutan Secara Menurun dalam lists
#list menurun adalah daftar yang diurutkan dari nilai terbesar ke terkecil misal dari (Z-A)
#Untuk mengurutkan secara menurun, gunakan argumen kata kunci reverse = True
nama = ["jeno", "shafwa", "choihyunwook", "jungwoon"]
nama.sort(reverse = True)
print(nama)

#sesuaikan fungsi pengurutan
#kita dapat menyusuaikan fungsi kita sendiri dengan menggunakan argumen kata kunci key = function
#fungsi ini akan mengembalikan angka yang akan digunakan untuk mengurutkan daftar (angka terendah terlebih dahulu)
#contohnya say mau mengurutkan daftar berdasarkan seberapa dekat angka tersebut dengan 25
def myfunc(n):
  return abs(n - 25)
numbers = [23, 26, 28, 24, 30]
numbers.sort(key = myfunc)
print(numbers)

print("---menyalin daftar---")
#menggunakan metode copy()
#copy() digunakan untuk menyalin sebuah daftar
nama = ["jeno", "shafwa", "choihyunwook", "jungwoon"]
nama2 = nama.copy()
print(nama2)

print("---menggabungkan list---")
#Ada beberapa cara untuk menggabungkan, atau menyatukan, dua atau lebih daftar di Python.
#Salah satu cara termudah adalah dengan menggunakan + operator.
#gabungkan dua daftar
buah1 = ["anggur", "apel", "nangka", "alpukat"]
buah2 = ["naga", "pepaya", "pisang"]

buah3 = buah1 + buah2
print(buah3)
#Cara lain untuk menggabungkan dua daftar adalah dengan menambahkan semua item dari daftar2 ke daftar1, satu per satu.
buah1 = ["anggur", "apel", "nangka", "alpukat"]
buah2 = ["naga", "pepaya", "pisang"]
for j in buah2:
    buah1.append(j)
print(buah1)