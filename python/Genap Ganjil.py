def cek_angka(angka):
    if angka % 2 == 0:
        print("Genap")
    else:
        print("Ganjil")

bilangan = int(input("angka:"))
cek_angka(bilangan)