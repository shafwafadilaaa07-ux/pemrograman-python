print("---latihan tuple---")
#tuple digunakan untuk menyimpan beberapa item dalam satu variabel.
#Tuple adalah salah satu dari 4 tipe data bawaan di Python yang digunakan untuk menyimpan kumpulan data, 3 lainnya adalah List , Set , dan Dictionary , yang semuanya memiliki kualitas dan penggunaan yang berbeda.
#Tuple adalah kumpulan yang terurut dan tidak dapat diubah .
#Tuple ditulis dengan tanda kurung.
#Tuple bersifat tidak dapat diubah, artinya kita tidak dapat mengubah, menambah, atau menghapus item setelah tuple dibuat.

lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
print(lagu)
#Karena tuple diindeks, maka tuple dapat memiliki item dengan nilai yang sama
lagu = ("young and beautiful", "like we just met", "lovely", "young and beautiful", "chanel")
print(lagu)

print("---mengakses item tuple---")
#kia dapat mengakses item tuple dengan merujuk pada nomor indeks, yang berada di dalam tanda kurung siku:
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
print(lagu[3])
#pengindeksan negatif
#pengindeksan negatif berarti dimulai dari akhir
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
print(lagu[-2])
#rentang indeks
#kita dapat menentukan rentang indeks dengan menentukan di mana rentang tersebut dimulai dan di mana rentang tersebut berakhir.
#Saat menentukan rentang, nilai yang dikembalikan akan berupa tuple baru dengan item yang ditentukan.
#kembalikan item kedua, ketiga, dan keempat
lagu = ("young and beautiful", "like we just met", "lovely", "chanel", "big boy", "drama")
print(lagu[2:5]) #dimulai dari indeks ke 2 dan berakhir di indeks ke 5 tapi tidak termasuk jadinya sampe ke indeks 4

print("---memperbarui tuple---")
#mengubah nilai tuple
#Setelah sebuah tuple dibuat, Anda tidak dapat mengubah nilainya. Tuple bersifat tidak dapat diubah , atau disebut juga immutable .
#Namun ada cara lain. kita dapat mengubah tuple menjadi list, mengubah list tersebut, dan mengubah list tersebut kembali menjadi tuple.
j = ("young and beautiful", "like we just met", "lovely", "chanel")
s = list (j)
s[1] = "salvatore"
j = tuple (s)
print(j)
#tambahkan item
#Karena tuple bersifat immutable (tidak dapat diubah), tuple tidak memiliki metode bawaan append(), tetapi ada cara lain untuk menambahkan item ke tuple.
#1. Konversi menjadi daftar : Sama seperti cara mengubah tuple, Anda dapat mengonversinya menjadi daftar, menambahkan item Anda, dan mengonversinya kembali menjadi tuple.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
j = list(lagu)
j.append("salvatore")
lagu = tuple(j)
print(lagu)
#2. Menambahkan tuple ke tuple . Anda diperbolehkan menambahkan tuple ke tuple, jadi jika Anda ingin menambahkan satu item (atau banyak), buat tuple baru dengan item tersebut, dan tambahkan ke tuple yang sudah ada.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
j = ("salvatore", "angel baby")
lagu += j
print(lagu)
#menghapus item
#Tuple bersifat tetap , jadi Anda tidak dapat menghapus item darinya, tetapi Anda dapat menggunakan solusi yang sama seperti yang kita gunakan untuk mengubah dan menambahkan item tuple.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
j = list(lagu)
j.remove("chanel")
lagu = tuple(j)
print(lagu)

print("---menguraikan tuple---")
lagu = ("young and beautiful", "like we just met", "lovely")
(green, yellow, red) = lagu
print(green)
print(yellow)
print(red)
#Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam tuple. Jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan nilai-nilai yang tersisa sebagai sebuah daftar.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel", "angel baby")
(green, yellow, *red) = lagu
print(green)
print(yellow)
print(red)

print("---perulangan tuple---")
#mengulang melalui tuple
#kita dapat mengulang melalui item tuple dengan menggunakan for perulangan.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
for j in lagu:
    print(j)
#perulangan melalui nomer indeks
#kita juga dapat melakukan perulangan melalui item tuple dengan merujuk pada nomor indeksnya.
#Gunakan fungsi ` range()and` len()untuk membuat objek iterable yang sesuai.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
for j in range(len(lagu)):
    print(lagu[j])
    
print("---menggabungkan tuple---")
#gabungkan dua tuple
#Untuk menggabungkan dua atau lebih tupel, Anda dapat menggunakan + operator.
lagu1 = ("young and beautiful", "like we just met", "lovely", "chanel")
lagu2 = ("salvatore", "angel baby", "drama")
lagu3 = lagu1 + lagu2
print(lagu3)
#mengalikan tuple
#Jika Anda ingin mengalikan isi sebuah tuple sebanyak jumlah tertentu, Anda dapat menggunakan * operator.
lagu = ("young and beautiful", "like we just met", "lovely", "chanel")
mytuple = lagu * 2
print(mytuple)
