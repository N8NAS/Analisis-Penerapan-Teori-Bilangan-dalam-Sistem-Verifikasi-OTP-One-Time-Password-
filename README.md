# Analisis Penerapan Teori Bilangan dalam Sistem Verifikasi OTP (One-Time Password)

Repository ini berisi implementasi dan analisis penerapan konsep-konsep dasar (seperti operasi *bitwise*, fungsi *hash* kriptografis, dan aljabar modular) dalam sistem verifikasi **One-Time Password (OTP)**. 

Di dalam repository ini, terdapat dua implementasi algoritma OTP dengan menggunakan bahasa pemrograman Python:
1. **HOTP (HMAC-based One-Time Password)** - OTP yang berbasis *counter* (penghitung). Mengacu pada spesifikasi standar RFC 4226.
2. **TOTP (Time-based One-Time Password)** - OTP yang berbasis pada waktu (*time-based*). Mengacu pada spesifikasi standar RFC 6238.

## Struktur Repository

```text
├── docs/          # Dokumentasi (jika ada)
├── src/           # Kode sumber implementasi OTP
│   ├── HOTP.py    # Skrip implementasi algoritma HMAC-based OTP
│   └── TOTP.py    # Skrip implementasi algoritma Time-based OTP
└── README.md      # Dokumentasi repository ini
```

## Prasyarat (Requirements)

- Membutuhkan **Python 3.x** terinstal pada sistem komputer Anda.
- Kode ini sepenuhnya menggunakan pustaka standar bawaan Python (seperti `hmac`, `hashlib`, `base64`, `struct`, `time`, dan `random`). Anda **tidak perlu** menginstal modul pihak ketiga (tanpa `pip install`).

## Cara Menjalankan Program

### 1. Simulasi HOTP (HMAC-based OTP)

Skrip `HOTP.py` mensimulasikan pembuatan kode OTP yang bergantung pada kunci rahasia (*secret key*) dan nilai *counter* yang di-*generate* secara acak (pada simulasi ini).

Buka terminal atau *command prompt*, arahkan (*cd*) ke direktori repository, lalu jalankan:
```bash
python src/HOTP.py
```
Program akan menghasilkan sebuah kode OTP 6 digit, mencetaknya ke layar, dan meminta pengguna untuk memasukkannya kembali untuk memverifikasi kecocokan kodenya.

### 2. Simulasi TOTP (Time-based OTP)

Skrip `TOTP.py` mensimulasikan pembuatan kode OTP yang bergantung pada kunci rahasia (*secret key*) dan *timestamp* (waktu saat ini), dengan periode batas waktu (interval) standar selama 30 detik.

Jalankan perintah berikut di terminal:
```bash
python src/TOTP.py
```
Sama seperti simulasi HOTP, program akan mencetak kode TOTP yang berlaku untuk rentang waktu saat ini dan kemudian meminta Anda untuk memasukkan input verifikasi.

## Konsep Teori Bilangan yang Digunakan

Walaupun terlihat didominasi oleh kriptografi, kedua algoritma ini memanfaatkan beberapa pilar operasi matematis yang sangat erat dengan teori bilangan:
- **Aritmetika Modular (Modulo)**: Pada tahap *Dynamic Truncation* (di akhir fungsi `buat_otp` dan `buat_totp`), terdapat operasi modulo berupa `kode % 10**digits`. Operasi modulo ini berguna untuk memangkas angka desimal (integer besar hasil *unpack* dari *hash*) menjadi kode yang lebih ringkas sepanjang digit yang ditentukan (contoh: 6 digit) sehingga mudah untuk dibaca dan diketik oleh manusia.
- **Operasi Bitwise dan Hashing**: Fungsi *hash* (SHA-1) dan fungsi *Dynamic Truncation* mengekstrak serangkaian panjang teks acak (*hash bytes*) dengan memanipulasinya menggunakan operator *bitwise* seperti AND (`& 0x0F`, `& 0x7FFFFFFF`) untuk menyembunyikan sign/tanda bit (memastikan bahwa integer yang dibaca positif dan diproses dalam batasan ukuran tertentu).
