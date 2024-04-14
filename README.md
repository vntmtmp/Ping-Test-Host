# Ping-Test-Host
Sebuah skrip sederhana untuk memeriksa konektivitas dan konfigurasi server

## Cara Penggunaan
- Pastikan Anda memiliki file `ip.txt` yang berisi daftar IP yang ingin Anda periksa. Setiap IP harus ditulis dalam baris yang berbeda.
- Jalankan skrip dengan perintah berikut: 
```bash
  python ping.py
```
- Hasil pemeriksaan akan disimpan dalam file `reachable.txt`, yang akan menampilkan status ping, status port 80 dan 443, serta informasi apakah server berjalan di Cloudflare atau tidak.
