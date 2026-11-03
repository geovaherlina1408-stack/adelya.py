print("================================")
print("         TES LOGIKA MTK")
print("================================")
print("1. Nilai Siswa")
print("2. Pembelian Barang")

pilihan = int(input("Pilih menu (1/2): "))

if pilihan == 1:
    print("\n=== NILAI SISWA ===")

    nama = input("Masukkan nama siswa: ")
    nilai1 = float(input("Nilai Matematika: "))
    nilai2 = float(input("Nilai Bahasa Indonesia: "))
    nilai3 = float(input("Nilai Bahasa Inggris: "))

    rata = (nilai1 + nilai2 + nilai3) / 3

    print("\nNama:", nama)
    print("Rata-rata:", rata)

    if rata >= 75:
        print("Keterangan: LULUS")
    else:
        print("Keterangan: TIDAK LULUS")

elif pilihan == 2:
    print("\n=== PEMBELIAN BARANG ===")
    print("1. Buku      = Rp5.000")
    print("2. Pensil    = Rp3.000")
    print("3. Penghapus = Rp2.000")
    print("4. Penggaris = Rp4.000")

    barang = int(input("Pilih barang (1-4): "))
    jumlah = int(input("Masukkan jumlah barang: "))

    if barang == 1:
        nama_barang = "Buku"
        harga = 5000
    elif barang == 2:
        nama_barang = "Pensil"
        harga = 3000
    elif barang == 3:
        nama_barang = "Penghapus"
        harga = 2000
    elif barang == 4:
        nama_barang = "Penggaris"
        harga = 4000
    else:
        print("Pilihan barang tidak tersedia!")
        exit()

    total = harga * jumlah

    print("\n=== STRUK PEMBELIAN ===")
    print("Nama barang:", nama_barang)
    print("Harga satuan: Rp", harga)
    print("Jumlah barang:", jumlah)
    print("Total pembayaran: Rp", total)

else:
    print("Pilihan tidak tersedia!")