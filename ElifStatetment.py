#struktur kendali elif
# jika nilai > 85 maka mendapat nilai A
# jika nilai >= 75 maka mendapat nilai B
# jika nilai >= 65 maka mendapat nilai C
# jika nilai >= 55 maka mendapat nilai D
# jika nilai < 55 maka mendapat nilai E
nilai = int(input("Masukkan nilai anda: "))

if(nilai > 85 and nilai <= 100):
    print("Anda mendapat nilai A")
elif(nilai >= 75 and nilai <= 85):
    print("Anda mendapat nilai B")
elif(nilai >= 65 and nilai < 75):
    print("Anda mendapat nilai C")
elif(nilai >= 55 and nilai < 65):
    print("Anda mendapat nilai D")
elif(nilai < 55 and nilai >= 0):
    print("Anda mendapat nilai E")
else:
    print("Masukkan nilai 0 - 100")