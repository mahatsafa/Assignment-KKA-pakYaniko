status = "up"
if status.lower() == "up":
    print("Perangkat aktif")
elif status == "down":
    print("Perangkat mati!")
else:
    print("Status tidak diketahui")