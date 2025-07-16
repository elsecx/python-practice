siswa = [
    {"nama": "Elgin", "nilai": 80},
    {"nama": "Dina", "nilai": 90}
]

def tampilkan_menu():
    print("\nMenu:")
    print("1. Tambah data siswa")
    print("2. Tampilkan semua data siswa")
    print("3. Hitung rata-rata nilai seluruh siswa")
    print("0. Keluar")

def tambah_siswa():
    nama = input("Masukkan nama siswa: ")
    nilai = int(input("Masukkan nilai siswa: "))
    siswa.append({"nama": nama, "nilai": nilai})
    print("✅ Siswa berhasil ditambahkan!")

def tampilkan_siswa():
    if not siswa:
        print("Belum ada data siswa.")
        return
    for s in siswa:
        print(f"- {s['nama']} (Nilai: {s['nilai']})")

def average():
    if not siswa:
        return 0
    total = sum(s["nilai"] for s in siswa)
    return total / len(siswa)

while True:
    tampilkan_menu()
    pilihan = input("Masukkan pilihan anda: ")

    if pilihan == "1":
        tambah_siswa()
    elif pilihan == "2":
        tampilkan_siswa()
    elif pilihan == "3":
        print(f"📊 Rata-rata nilai seluruh siswa: {average():.2f}")
    elif pilihan == "0":
        print("👋 Keluar dari program.")
        break
    else:
        print("❌ Pilihan tidak valid. Silakan coba lagi.")
