devices = ["bima", "gusto", "mahatsafa", "moklet", "telkom"]
koordinat = (10, 5)
print("Perangkat pertama:", devices[0])
print("Perangkat terakhir:", devices[-1])

data = {
    "bima": {
        "nama": "Bima",
        "ip": "192.168.1.1",
        "status": "up"
    },
    "gusto": {
        "nama": "Gusto",
        "ip": "192.168.1.2",
        "status": "up"
    },
    "mahatsafa": {
        "nama": "Mahatsafa",
        "ip": "192.168.1.3",
        "status": "down"
    },
    "moklet": {
        "nama": "Moklet",
        "ip": "192.168.1.4",
        "status": "up"
    },
    "telkom": {
        "nama": "Telkom",
        "ip": "192.168.1.5",
        "status": "down"
    }
}

for key, value in data.items():
    print(key, ":", value)

def cek_status(nama, status):
    if status == "up":
        return f"Perangkat {nama} aktif"
    else:
        return f"Perangkat {nama} tidak aktif"


print(cek_status("Bima", "up"))
print(cek_status("Gusto", "up"))
print(cek_status("Mahatsafa", "down"))

def cek_semua(data):
    for key, perangkat in data.items():
        print(perangkat["nama"], ":", perangkat["status"])


def hitung_aktif(data):
    jumlah = 0

    for key, perangkat in data.items():
        if perangkat["status"] == "up":
            jumlah += 1

    return jumlah


cek_semua(data)
print("Jumlah perangkat aktif:", hitung_aktif(data))