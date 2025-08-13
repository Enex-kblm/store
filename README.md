# 🛒 Aplikasi Toko Sederhana - Panduan Lengkap

## 📋 Apa itu Program Ini?

Program ini adalah **aplikasi kasir sederhana** yang dibuat dengan bahasa Python. Bayangkan Anda memiliki toko kecil dan butuh sistem untuk:
- Menampilkan daftar barang dan harga
- Melayani pembeli
- Menghitung kembalian secara otomatis
- Mencetak struk pembelian

Program ini akan melakukan semua itu untuk Anda!

## 🎯 Fitur Utama

✅ **Daftar Barang Otomatis** - Menampilkan semua barang yang dijual  
✅ **Input Nama Pembeli** - Mencatat siapa yang berbelanja  
✅ **Pencarian Barang** - Mengecek apakah barang tersedia  
✅ **Perhitungan Otomatis** - Menghitung kembalian tanpa ribet  
✅ **Struk Digital** - Menampilkan struk pembelian yang rapi  
✅ **Format Rupiah** - Menampilkan harga dalam format yang mudah dibaca  

## 🏪 Barang yang Dijual

| Nama Barang | Harga |
|-------------|-------|
| Pulpen | Rp. 5.000 |
| Pensil | Rp. 2.500 |
| Penggaris | Rp. 7.000 |
| Penghapus | Rp. 1.500 |
| Buku | Rp. 25.000 |

## 🚀 Cara Menggunakan Program

1. **Jalankan program** - Program akan menyapa Anda
2. **Lihat daftar barang** - Program menampilkan semua barang yang dijual
3. **Masukkan nama Anda** - Ketik nama pembeli
4. **Pilih barang** - Ketik nama barang yang ingin dibeli
5. **Bayar** - Masukkan jumlah uang yang dibayarkan
6. **Terima struk** - Program akan menampilkan struk dan kembalian

## 📖 Penjelasan Kode (Untuk yang Ingin Belajar)

### 🏷️ Bagian 1: Menyiapkan Data Barang (Baris 1-7)

```python
item = {
"pulpen": 5000,
"pensil": 2500,
"penggaris": 7000,
"penghapus": 1500,
"buku": 25000
}
```

**Penjelasan Sederhana:**
- Ini seperti membuat **daftar harga** di kertas
- `item` adalah nama daftar barang kita
- Setiap barang punya nama dan harga
- Contoh: "pulpen" harganya 5000 rupiah

### 👋 Bagian 2: Menyapa Pembeli (Baris 9-13)

```python
print("Selamat datang di toko kami\n")
print("Ini list barang yang kita jual:")

for nama_barang in item.keys():
    print(f"• {nama_barang}")
```

**Penjelasan Sederhana:**
- `print()` = perintah untuk menampilkan tulisan di layar
- Program menyapa pembeli dengan ramah
- `for` = perintah untuk mengulang sesuatu
- Program menampilkan semua nama barang satu per satu dengan tanda bullet (•)

### 📝 Bagian 3: Mengambil Data Pembeli (Baris 15-17)

```python
nama = input("\nMasukkan nama anda: ")
barang = input("Masukkan barang yang ingin anda beli: ").lower()
```

**Penjelasan Sederhana:**
- `input()` = perintah untuk meminta pengguna mengetik sesuatu
- `nama` = tempat menyimpan nama pembeli
- `barang` = tempat menyimpan nama barang yang ingin dibeli
- `.lower()` = mengubah huruf besar jadi huruf kecil (agar tidak salah ketik)

### 🔍 Bagian 4: Mengecek Barang (Baris 19)

```python
if barang in item:
```

**Penjelasan Sederhana:**
- `if` = perintah "jika"
- Program mengecek: "Jika barang yang diminta ada di toko..."
- Seperti kasir yang mengecek apakah barang masih tersedia

### 💰 Bagian 5: Menampilkan Harga dan Meminta Pembayaran (Baris 20-23)

```python
harga = item[barang]
print(f"Harga {barang} adalah Rp. {harga:,}".replace(",", "."))
dibayar = int(input("Masukkan jumlah uang dibayar: "))
```

**Penjelasan Sederhana:**
- `harga = item[barang]` = mengambil harga barang dari daftar
- Program memberitahu harga barang
- `:,` dan `.replace(",", ".")` = membuat format rupiah (5.000 bukan 5000)
- `int()` = mengubah tulisan jadi angka
- Program meminta pembeli memasukkan uang

### ✅ Bagian 6: Mengecek Uang Cukup atau Tidak (Baris 25)

```python
if dibayar >= harga:
```

**Penjelasan Sederhana:**
- `>=` = lebih besar atau sama dengan
- Program mengecek: "Apakah uang yang dibayar cukup?"
- Seperti kasir yang memastikan pembayaran cukup

### 🧮 Bagian 7: Menghitung Kembalian (Baris 26)

```python
kembalian = dibayar - harga
```

**Penjelasan Sederhana:**
- Kembalian = Uang yang dibayar - Harga barang
- Contoh: Bayar 10.000, harga 7.000, kembalian = 3.000

### 🧾 Bagian 8: Mencetak Struk (Baris 28-34)

```python
print("\n===== STRUK PEMBELIAN =====")
print(f"Nama      : {nama}")
print(f"Beli      : {barang}")
print(f"Tagihan   : Rp. {harga:,}".replace(",", "."))
print(f"Dibayar   : Rp. {dibayar:,}".replace(",", "."))
print(f"Kembalian : Rp. {kembalian:,}".replace(",", "."))
print("===========================")
```

**Penjelasan Sederhana:**
- Program membuat struk pembelian yang rapi
- Menampilkan semua informasi: nama, barang, harga, pembayaran, kembalian
- Seperti struk yang Anda terima di toko sungguhan

### ❌ Bagian 9: Menangani Kesalahan (Baris 36-40)

```python
else:
    print("Uang tidak cukup untuk membeli barang ini.")
else:
    print("Barang tidak ditemukan.")
```

**Penjelasan Sederhana:**
- `else` = "jika tidak" atau "selain itu"
- Jika uang tidak cukup → tampilkan pesan "uang tidak cukup"
- Jika barang tidak ada → tampilkan pesan "barang tidak ditemukan"

## 🎮 Contoh Penggunaan

```
Selamat datang di toko kami

Ini list barang yang kita jual:
• pulpen
• pensil  
• penggaris
• penghapus
• buku

Masukkan nama anda: Budi
Masukkan barang yang ingin anda beli: pulpen
Harga pulpen adalah Rp. 5.000
Masukkan jumlah uang dibayar: 10000

===== STRUK PEMBELIAN =====
Nama      : Budi
Beli      : pulpen
Tagihan   : Rp. 5.000
Dibayar   : Rp. 10.000
Kembalian : Rp. 5.000
===========================
```

## 🎓 Apa yang Bisa Dipelajari?

Dari program sederhana ini, Anda bisa belajar:

1. **Dictionary** - Cara menyimpan data berpasangan (nama-harga)
2. **Input/Output** - Cara berinteraksi dengan pengguna
3. **Conditional (if-else)** - Cara membuat keputusan dalam program
4. **Loop (for)** - Cara mengulang perintah
5. **String Formatting** - Cara menampilkan data dengan rapi
6. **Error Handling** - Cara menangani kesalahan input

## 🔧 Cara Menjalankan Program

1. Pastikan Python sudah terinstall di komputer
2. Simpan kode dalam file `index.py`
3. Buka terminal/command prompt
4. Ketik: `python index.py`
5. Ikuti instruksi yang muncul di layar

## 💡 Tips untuk Pengembangan

- Tambahkan lebih banyak barang
- Buat sistem diskon
- Tambahkan fitur stok barang
- Simpan data transaksi ke file
- Buat tampilan yang lebih menarik

---

**Selamat belajar coding! 🚀**