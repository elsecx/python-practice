nama = input("Masukkan nama siswa: ")
nilai = int(input("Masukkan nilai ujian siswa: "))

print(f"Siswa: {nama}")
print(f"Nilai: {nilai}")

if nilai >= 90:
    print(f"Status: Nilai A (Lulus) {nama} kamu Hebat!")
elif nilai >= 75:
    print("Status: Nilai B (Lulus)")
elif nilai >= 60:
    print("Status: Nilai C (Lulus bersyarat)")
else:
    print(f"Status: {nama} TIDAK LULUS!")