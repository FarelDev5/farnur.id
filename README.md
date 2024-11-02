# farnur.id
Termux Hacking Tools

Berikut adalah `README.md` yang lebih sesuai untuk *tools* **Farnur** sebagai pengubah tampilan Termux sekaligus menambah beberapa fitur khusus.

```markdown
# Farnur Tool

## Deskripsi
**Farnur** adalah tools untuk mengubah tampilan Termux agar menyerupai terminal Linux, sekaligus dilengkapi dengan fitur tambahan untuk kebutuhan pengguna. Dengan *Farnur*, tampilan Termux Anda akan lebih menarik dengan skema warna abu-abu-putih serta pesan kesalahan yang ditampilkan dalam warna merah, memberikan pengalaman yang lebih realistis layaknya terminal Linux. Selain itu, Farnur memiliki fitur untuk menampilkan informasi IP, koneksi DNS, dan beberapa fitur menarik lainnya.

## Fitur Utama
- **Kustomisasi Tampilan**: Mengubah tampilan Termux menjadi lebih mirip terminal Linux.
- **Informasi Jaringan**: Menampilkan informasi IP dan koneksi DNS.
- **Kompatibilitas Perintah**: Mendukung perintah-perintah dasar Termux dan Linux.
- **Penginstalan Paket**: Mempermudah instalasi paket yang sering digunakan.
- **Fitur Lainnya**: Menyediakan fitur tambahan yang membantu pengguna dalam aktivitas terminal.

## Instalasi
Berikut adalah langkah-langkah untuk menginstal **Farnur** di Termux:

1. **Perbarui Paket dan Install Git**
   ```bash
   pkg update && pkg upgrade
   pkg install git -y
   ```

2. **Clone Repository Farnur**
   ```bash
   git clone https://github.com/FarelDev5/farnur.id
   ```

3. **Masuk ke Direktori Farnur**
   ```bash
   cd farnur.id
   ```

4. **Jalankan Script**
   Eksekusi `farnur.py` untuk mengaktifkan tools dan menyesuaikan tampilan:
   ```bash
   python3 farnur.py
   ```

## Cara Penggunaan
Setelah `farnur.py` berjalan, Anda dapat menggunakan perintah-perintah dengan format sebagai berikut:
```
Farnur/cmd: <perintah_anda>
```

Contoh:
```bash
Farnur/cmd: ls
```

Anda juga bisa mengakses fitur khusus untuk menampilkan informasi jaringan atau menggunakan perintah lainnya yang tersedia di dalam tools ini.

## Catatan
- **Farnur** membutuhkan **Python 3** agar dapat berjalan dengan baik.
- Pastikan koneksi internet stabil saat pertama kali menginstal agar semua paket terpasang dengan benar.
- Jika terdapat kendala, silakan ajukan di bagian *Issues* di [GitHub Repository](https://github.com/FarelDev5/farnur.id).

## Kontribusi
Kontribusi sangat dihargai! Jika Anda ingin menambahkan fitur atau perbaikan, buatlah *pull request* atau laporkan pada bagian *Issues*.

---

Dikembangkan oleh Farel Alfareza.
```

Template ini bisa disesuaikan sesuai dengan tambahan fitur atau kebutuhan yang spesifik dari tools Farnur.
