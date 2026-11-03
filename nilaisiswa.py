print("====================================")
print("          TES LOGIKA MTK")
print("       NILAI RATA-RATA SISWA")
print("====================================")

nama = input("Masukkan nama siswa: ")
kelas = input("Masukkan kelas: ")

print("\n=== MASUKKAN NILAI MATA PELAJARAN ===")

mtk = float(input("Nilai Matematika: "))
bindo = float(input("Nilai Bahasa Indonesia: "))
bing = float(input("Nilai Bahasa Inggris: "))
pai = float(input("Nilai PAI: "))
informatika = float(input("Nilai Informatika: "))

total = mtk + bindo + bing + pai + informatika
rata_rata = total / 5

print("\n====================================")
print("          HASIL NILAI SISWA")
print("====================================")

print("Nama siswa:", nama)
print("Kelas:", kelas)
print("Matematika:", mtk)
print("Bahasa Indonesia:", bindo)
print("Bahasa Inggris:", bing)
print("PAI:", pai)
print("Informatika:", informatika)

print("------------------------------------")
print("Total nilai:", total)
print("Nilai rata-rata:", round(rata_rata, 2))
print("====================================")