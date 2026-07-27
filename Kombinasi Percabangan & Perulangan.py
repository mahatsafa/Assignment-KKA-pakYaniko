pemakaian = [45, 85, 60, 92, 78]
batas = 80
peringatan = 0
for p in pemakaian:
    if p > batas:
        print(f"{p}: PERINGATAN")
        peringatan += 1
    else:
        print(f"{p}: normal")
print(f"Total PERINGATAN: {peringatan}")