def tentukan(angka):
  if angka % 2 == 0:
    hasil = "genap"
  else:
    hasil = "ganjil"
  return hasil
def cek_angka(angka, pilihan):
  hasil = tentukan(angka)
  if pilihan == "1":
    pilihan = "ganjil"
  else:
    pilihan = "genap"
  if pilihan == hasil:
    print(f"{angka}{hasil}")
  else:
    print(f"{angka}bukan{pilihan}")
pilihan = input("1 gannjil 2 genaap")
bilangan = int(input("masukkan angka"))
cek_angka(bilangan, pilihan)