# Farnur Tool

## Deskripsi
**Farnur** adalah tools untuk mengubah tampilan Termux agar menyerupai terminal Linux, dilengkapi dengan berbagai fitur tambahan. Farnur tidak hanya memodifikasi tampilan, tetapi juga menyediakan fitur khusus seperti informasi IP, koneksi DNS, dan lainnya, yang membantu pengguna dalam aktivitas terminal di Termux.

## Fitur Utama
- **Kustomisasi Tampilan**: Menyesuaikan tampilan Termux agar lebih mirip terminal Linux.
- **Informasi Jaringan**: Menampilkan informasi IP dan koneksi DNS.
- **Kompatibilitas Perintah**: Mendukung perintah-perintah dasar Termux dan Linux.
- **Penginstalan Paket**: Mudah menginstal berbagai paket yang diperlukan untuk pengoperasian Termux.
- **Fitur Tambahan**: Fitur tambahan yang dirancang untuk meningkatkan pengalaman pengguna di Termux.

## Persyaratan
Pastikan Anda memiliki **Python 3** yang sudah terinstal di Termux.

## Instalasi
Ikuti langkah-langkah berikut untuk menginstal **Farnur** beserta semua bahan yang dibutuhkan:

1. **Perbarui Paket dan Install Git**
   ```bash
   pkg update && pkg upgrade
   pkg install git -y
   ```

2. **Clone Repository Farnur**
   Clone repositori Farnur dari GitHub:
   ```bash
   git clone https://github.com/FarelDev5/farnur.id
   ```

3. **Masuk ke Direktori Farnur**
   Pindah ke direktori `farnur.id`:
   ```bash
   cd farnur.id
   ```

4. **Instal Semua Bahan yang Dibutuhkan**
   Tools Farnur mungkin memerlukan beberapa paket tambahan agar berfungsi dengan baik. Instal semua bahan yang diperlukan dengan menjalankan:
   ```bash
   bash install.sh
   ```
   atau jika `install.sh` belum ada, pastikan instal paket berikut:
   ```bash
   pkg install python python3-pip -y
   pip install requests
   ```

5. **Jalankan Script**
   Setelah semua bahan terpasang, Anda dapat menjalankan tools dengan perintah:
   ```bash
   python3 farnur.py
   ```

## Cara Penggunaan
Setelah `farnur.py` dijalankan, Anda bisa mulai menggunakan perintah-perintah di tools ini dengan format:
```
Farnur/cmd: <perintah_anda>
```

Contoh:
```bash
Farnur/cmd: ls
```

Anda juga dapat mengakses fitur tambahan yang telah disediakan oleh Farnur untuk menampilkan informasi jaringan atau menjalankan perintah lainnya.

## Catatan
- **Farnur** dirancang untuk bekerja optimal di Termux dengan tampilan menyerupai terminal Linux.
- Pastikan semua paket terpasang dengan benar untuk menghindari error.

## Kontribusi
Jika Anda ingin berkontribusi, silakan buat *pull request* atau buka *issue* di [GitHub Repository](https://github.com/FarelDev5/farnur.id).

---

Dikembangkan oleh Farel Alfareza.
```

Gunakan dengan bijak.
tools ini di gunakan untuk belajar
saya tidak bertanggung jawab jika di salah gunakan
semua tergantung dari bagaimana cara kamu menggunakan tools ini
