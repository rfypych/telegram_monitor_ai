# Panduan Testing: Mode Live (Telegram Asli)

Selamat! Karena Anda sudah memiliki `API_ID` dan `API_HASH`, Anda sekarang bisa menjalankan bot ini dengan data Telegram sungguhan.

## Langkah 1: Masukkan Kunci Rahasia

1.  Buka file bernama `.env` di dalam folder proyek ini.
2.  Cari baris `API_ID` dan `API_HASH`.
3.  Hapus tulisan defaultnya dan ganti dengan angka/kode dari my.telegram.org.

Contoh yang benar:
```env
API_ID=12345678
API_HASH=a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6
SESSION_NAME=sesi_monitor_saya
TARGET_CHANNELS=@katalog_promo,@info_diskon_id
GROQ_API_KEY=gsk_... (Jika ada, biarkan kosong jika tidak)
```

> **Penting**: Jangan gunakan tanda kutip (`"` atau `'`) kecuali jika kodenya mengandung spasi (jarang terjadi).

## Langkah 2: Jalankan Script

Buka terminal/command prompt di folder `telegram_monitor_mvp`, lalu ketik:

```bash
python -m src.monitor
```

## Langkah 3: Login (Hanya Sekali)

Karena ini pertama kalinya Anda menghubungkan script ke akun Telegram Anda, script akan meminta verifikasi:

1.  **Please enter your phone (or bot token):**
    Ketik nomor HP Anda dengan kode negara (contoh: `+628123456789`), lalu tekan Enter.

2.  **Please enter the code you received:**
    Cek aplikasi Telegram di HP Anda (biasanya dikirim oleh "Telegram Service Notification"). Masukkan kode angka tersebut di terminal, lalu tekan Enter.

3.  **Signed in successfully as ...**
    Jika berhasil, bot akan mulai berjalan dan memantau channel yang Anda tulis di `.env`!

## Tips Tambahan

*   **File Session**: Setelah login berhasil, akan muncul file baru bernama `sesi_monitor_saya.session`. Jangan hapus file ini agar Anda tidak perlu login ulang setiap kali menjalankan script.
*   **Keamanan**: Jangan pernah membagikan file `.session` atau isi `.env` Anda kepada orang lain.
*   **Error FloodWait**: Jika Anda terlalu sering login/logout atau mengambil data terlalu cepat, Telegram mungkin memblokir sementara (FloodWait). Jika ini terjadi, tunggu beberapa menit/jam sebelum mencoba lagi.

Selamat mencoba!
