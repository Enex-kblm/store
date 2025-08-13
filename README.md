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

### 🏷️ **Baris 1-7: Membuat Daftar Barang dengan Dictionary**

```python
# Baris 1: Membuat daftar dengan nama "item" - ini namanya dictionary
item = {
    "pulpen": 5000,      # Baris 2: pulpen harganya 5000
    "pensil": 2500,      # Baris 3: pensil harganya 2500  
    "penggaris": 7000,   # Baris 4: penggaris harganya 7000
    "penghapus": 1500,   # Baris 5: penghapus harganya 1500
    "buku": 25000        # Baris 6: buku harganya 25000
}
# Baris 7: Tutup kurung kurawal - selesai membuat dictionary
```

**Penjelasan Sederhana:**
- **Baris 1**: Membuat daftar dengan nama `item` - ini namanya **dictionary**
- **Dictionary** itu seperti kamus: ada kata (nama barang) dan artinya (harga)
- **Baris 2-6**: Setiap baris mendaftarkan satu barang dan harganya
- Format: `"nama_barang": harga` (nama barang dalam tanda petik, harga berupa angka)
- **Baris 7**: Menutup dictionary dengan kurung kurawal `}`

### 👋 **Baris 9-13: Menyapa Pembeli dan Menampilkan Daftar**

```python
print("Selamat datang di toko kami\n")    # Baris 9: Menyapa pembeli
print("Ini list barang yang kita jual:")  # Baris 10: Memberitahu akan tampil daftar

for nama_barang in item.keys():            # Baris 12: Ambil semua nama barang dari dictionary
    print(f"• {nama_barang}")              # Baris 13: Tampilkan setiap nama barang dengan bullet
```

**Penjelasan Sederhana:**
- **Baris 9**: `print()` menampilkan tulisan "Selamat datang" di layar
- **Baris 10**: Memberitahu bahwa akan menampilkan daftar barang
- **Baris 12**: `for` artinya "untuk setiap", `item.keys()` mengambil semua nama barang dari dictionary
- **Baris 13**: Menampilkan setiap nama barang dengan tanda bullet (•)

### 📝 **Baris 15-17: Mengambil Data dari Pembeli**

```python
nama = input("\nMasukkan nama anda: ")                              # Baris 15: Minta nama pembeli
barang = input("Masukkan barang yang ingin anda beli: ").lower()    # Baris 17: Minta nama barang
```

**Penjelasan Sederhana:**
- **Baris 15**: `input()` meminta pengguna mengetik nama, hasilnya disimpan di `nama`
- **Baris 17**: Meminta pengguna mengetik nama barang yang ingin dibeli
- `.lower()` mengubah huruf besar jadi kecil (contoh: "PULPEN" jadi "pulpen")
- Ini mencegah error kalau user salah ketik huruf besar/kecil

### 🔍 **Baris 19: Mengecek Apakah Barang Ada**

```python
if barang in item:    # Baris 19: Cek apakah barang yang diminta ada di dictionary
```

**Penjelasan Sederhana:**
- **Baris 19**: `if` artinya "jika", `in` artinya "ada di dalam"
- Program mengecek: "Jika barang yang diminta ada di dalam dictionary item..."
- Seperti kasir yang mengecek apakah barang ada di toko

### 💰 **Baris 20-23: Menampilkan Harga dan Meminta Pembayaran**

```python
harga = item[barang]                                                    # Baris 20: Ambil harga dari dictionary
print(f"Harga {barang} adalah Rp. {harga:,}".replace(",", "."))        # Baris 21: Tampilkan harga
dibayar = int(input("Masukkan jumlah uang dibayar: "))                  # Baris 23: Minta jumlah pembayaran
```

**Penjelasan Sederhana:**
- **Baris 20**: `item[barang]` mengambil harga dari dictionary berdasarkan nama barang
- **Baris 21**: Menampilkan harga dengan format rupiah (5.000 bukan 5000)
- `:,` membuat koma, `.replace(",", ".")` mengubah koma jadi titik
- **Baris 23**: `int()` mengubah tulisan jadi angka, `input()` meminta user mengetik jumlah uang

### ✅ **Baris 25: Mengecek Apakah Uang Cukup**

```python
if dibayar >= harga:    # Baris 25: Cek apakah uang yang dibayar cukup atau tidak
```

**Penjelasan Sederhana:**
- **Baris 25**: `>=` artinya "lebih besar atau sama dengan"
- Program mengecek: "Apakah uang yang dibayar >= harga barang?"
- Kalau iya, lanjut ke proses berikutnya. Kalau tidak, tampilkan pesan error

### 🧮 **Baris 26: Menghitung Kembalian**

```python
kembalian = dibayar - harga    # Baris 26: Hitung kembalian
```

**Penjelasan Sederhana:**
- **Baris 26**: Rumus sederhana: Kembalian = Uang dibayar - Harga barang
- Contoh: Bayar 10.000, harga 7.000, kembalian = 3.000
- Hasil perhitungan disimpan di variabel `kembalian`

### 🧾 **Baris 28-34: Mencetak Struk Pembelian**

```python
print("\n===== STRUK PEMBELIAN =====")                              # Baris 28: Header struk
print(f"Nama      : {nama}")                                        # Baris 29: Tampilkan nama
print(f"Beli      : {barang}")                                      # Baris 30: Tampilkan barang
print(f"Tagihan   : Rp. {harga:,}".replace(",", "."))              # Baris 31: Tampilkan harga
print(f"Dibayar   : Rp. {dibayar:,}".replace(",", "."))            # Baris 32: Tampilkan pembayaran
print(f"Kembalian : Rp. {kembalian:,}".replace(",", "."))          # Baris 33: Tampilkan kembalian
print("===========================")                                # Baris 34: Footer struk
```

**Penjelasan Sederhana:**
- **Baris 28**: Membuat header struk dengan garis pembatas
- **Baris 29-33**: Menampilkan detail transaksi (nama, barang, harga, dll)
- `f"..."` adalah format string, `{nama}` akan diganti dengan nilai variabel nama
- **Baris 34**: Membuat footer struk dengan garis pembatas

### ❌ **Baris 35-39: Menangani Kesalahan**

```python
else:                                                    # Baris 35: Kalau uang tidak cukup
    print("Uang tidak cukup untuk membeli barang ini.") # Baris 36: Tampilkan pesan error
else:                                                    # Baris 38: Kalau barang tidak ada
    print("Barang tidak ditemukan.")                    # Baris 39: Tampilkan pesan error
```

**Penjelasan Sederhana:**
- **Baris 35**: `else` artinya "kalau tidak" (kalau uang tidak cukup)
- **Baris 36**: Tampilkan pesan bahwa uang tidak mencukupi
- **Baris 38**: `else` kedua untuk kondisi barang tidak ditemukan
- **Baris 39**: Tampilkan pesan bahwa barang tidak ada di toko

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

## 👨‍💻 Author

**Julian**  
📱 Instagram: [@gtwuuyyy_](https://instagram.com/gtwuuyyy_)

---

**Selamat belajar coding! 🚀**