item = {
"pulpen": 5000,
"pensil": 2500,
"penggaris": 7000,
"penghapus": 1500,
"buku": 25000
}

print("Selamat datang di toko kami\n")
print("Ini list barang yang kita jual:")

for nama_barang in item.keys():
print(f"• {nama_barang}")

nama = input("\nMasukkan nama anda: ")

barang = input("Masukkan barang yang ingin anda beli: ").lower()

if barang in item:
harga = item[barang]
print(f"Harga {barang} adalah Rp. {harga:,}".replace(",", "."))

dibayar = int(input("Masukkan jumlah uang dibayar: "))  

if dibayar >= harga:  
    kembalian = dibayar - harga  
      
    print("\n===== STRUK PEMBELIAN =====")  
    print(f"Nama      : {nama}")  
    print(f"Beli      : {barang}")  
    print(f"Tagihan   : Rp. {harga:,}".replace(",", "."))  
    print(f"Dibayar   : Rp. {dibayar:,}".replace(",", "."))  
    print(f"Kembalian : Rp. {kembalian:,}".replace(",", "."))  
    print("===========================")  
else:  
    print("Uang tidak cukup untuk membeli barang ini.")

else:
print("Barang tidak ditemukan.")

tolong bikinin markdown untuk menjelaskan per line codenya dong

