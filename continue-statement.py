#latihan continue statement
#continue statement digunakan untuk melewati sisa kode pada perulangan saat ini dan langsung melanjutkan ke literasi berikutnya, tanpa menghentikan seluruh perulangan.

h = 0
while h < 6:
  h += 1
  if h == 3:
    continue #fungsi continue yaitu melewati satu putaran saja, lalu lanjut ke putaran selanjutnya
  print(h)