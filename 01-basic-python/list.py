siswa = []

while True:
    nama = input("Masukkan nama siswa (atau ketik 'selesai' untuk berhenti): ")
    if nama.lower() == "selesai":
        break
    siswa.append(nama)

for i, nama in enumerate(siswa, start=1):
    print(f"{i}. {nama}")