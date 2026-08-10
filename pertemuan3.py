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

def cek_status(data):
    print("status")

    for perangkat in data.values():
        print(f"{perangkat['nama']} | {perangkat['ip']} | {perangkat['status']}")

def hitung_ringkasan(data):
    aktif = 0
    tidak_aktif = 0

    for perangkat in data.values():
        if perangkat["status"] == "up":
            aktif += 1
        else:
            tidak_aktif += 1

    return aktif, tidak_aktif
aktif, tidak_aktif = hitung_ringkasan(data)

cek_status(data)
print(f"Perangkat aktif     : {aktif}")
print(f"Perangkat tidak aktif: {tidak_aktif}")
