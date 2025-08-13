# Penjelasan Kode Python - Aplikasi Toko Sederhana

## Deskripsi Program
Program ini adalah aplikasi toko sederhana yang memungkinkan pengguna untuk membeli barang dan menghitung kembalian.

## Penjelasan Kode per Baris

### Baris 1-6: Definisi Data Barang
```python
item = {
"pulpen": 5000,
"pensil": 2500,
"penggaris": 7000,
"penghapus": 1500,
"buku": 25000
}
```
- **Baris 1**: Membuat dictionary bernama `item` untuk menyimpan data barang
- **Baris 2**: Menambahkan item "pulpen" dengan harga 5000 rupiah
- **Baris 3**: Menambahkan item "pensil" dengan harga 2500 rupiah
- **Baris 4**: Menambahkan item "penggaris" dengan harga 7000 rupiah
- **Baris 5**: Menambahkan item "penghapus" dengan harga 1500 rupiah
- **Baris 6**: Menambahkan item "buku" dengan harga 25000 rupiah

### Baris 8-9: Pesan Selamat Datang
```python
print("Selamat datang di toko kami\n")
print("Ini list barang yang kita jual:")
```
- **Baris 8**: Menampilkan pesan selamat datang dengan baris kosong (`\n`)
- **Baris 9**: Menampilkan header untuk daftar barang

### Baris 11-12: Menampilkan Daftar Barang
```python
for nama_barang in item.keys():
print(f"• {nama_barang}")
```
- **Baris 11**: Loop untuk mengiterasi semua kunci (nama barang) dalam dictionary `item`
- **Baris 12**: Menampilkan setiap nama barang dengan bullet point (•)

### Baris 14-16: Input dari Pengguna
```python
nama = input("\nMasukkan nama anda: ")

barang = input("Masukkan barang yang ingin anda beli: ").lower()
```
- **Baris 14**: Meminta input nama pengguna dan menyimpannya dalam variabel `nama`
- **Baris 15**: Baris kosong untuk pemisah
- **Baris 16**: Meminta input nama barang yang ingin dibeli, mengkonversi ke huruf kecil dengan `.lower()`

### Baris 18: Pengecekan Ketersediaan Barang
```python
if barang in item:
```
- **Baris 18**: Mengecek apakah barang yang diminta ada dalam dictionary `item`

### Baris 19-21: Mengambil Harga dan Input Pembayaran
```python
harga = item[barang]
print(f"Harga {barang} adalah Rp. {harga:,}".replace(",", "."))

dibayar = int(input("Masukkan jumlah uang dibayar: "))
```
- **Baris 19**: Mengambil harga barang dari dictionary dan menyimpannya dalam variabel `harga`
- **Baris 20**: Menampilkan harga barang dengan format ribuan (titik sebagai pemisah)
- **Baris 21**: Baris kosong
- **Baris 22**: Meminta input jumlah uang yang dibayar dan mengkonversinya ke integer

### Baris 24: Pengecekan Kecukupan Uang
```python
if dibayar >= harga:
```
- **Baris 24**: Mengecek apakah uang yang dibayar cukup untuk membeli barang

### Baris 25: Menghitung Kembalian
```python
kembalian = dibayar - harga
```
- **Baris 25**: Menghitung kembalian dengan mengurangi harga dari uang yang dibayar

### Baris 27-34: Menampilkan Struk Pembelian
```python
print("\n===== STRUK PEMBELIAN =====")
print(f"Nama      : {nama}")
print(f"Beli      : {barang}")
print(f"Tagihan   : Rp. {harga:,}".replace(",", "."))
print(f"Dibayar   : Rp. {dibayar:,}".replace(",", "."))
print(f"Kembalian : Rp. {kembalian:,}".replace(",", "."))
print("===========================")
```
- **Baris 27**: Menampilkan header struk dengan baris kosong di awal
- **Baris 28**: Menampilkan nama pembeli
- **Baris 29**: Menampilkan nama barang yang dibeli
- **Baris 30**: Menampilkan tagihan dengan format ribuan
- **Baris 31**: Menampilkan jumlah uang yang dibayar dengan format ribuan
- **Baris 32**: Menampilkan kembalian dengan format ribuan
- **Baris 33**: Menampilkan footer struk

### Baris 35-36: Pesan Uang Tidak Cukup
```python
else:
    print("Uang tidak cukup untuk membeli barang ini.")
```
- **Baris 35**: Kondisi else jika uang tidak cukup
- **Baris 36**: Menampilkan pesan bahwa uang tidak cukup

### Baris 38-39: Pesan Barang Tidak Ditemukan
```python
else:
print("Barang tidak ditemukan.")
```
- **Baris 38**: Kondisi else jika barang tidak ada dalam dictionary
- **Baris 39**: Menampilkan pesan bahwa barang tidak ditemukan

## Fitur Program
1. **Daftar Barang**: Menampilkan semua barang yang tersedia
2. **Input Pengguna**: Meminta nama dan barang yang ingin dibeli
3. **Validasi**: Mengecek ketersediaan barang dan kecukupan uang
4. **Perhitungan**: Menghitung kembalian secara otomatis
5. **Struk**: Menampilkan struk pembelian yang lengkap
6. **Format Uang**: Menggunakan format ribuan dengan titik sebagai pemisah

## Cara Kerja Program
1. Program menampilkan daftar barang dan harga
2. Pengguna memasukkan nama dan barang yang ingin dibeli
3. Program mengecek apakah barang tersedia
4. Jika tersedia, program meminta jumlah pembayaran
5. Program mengecek apakah uang cukup
6. Jika cukup, program menampilkan struk dan kembalian
7. Jika tidak, program menampilkan pesan error yang sesuai
