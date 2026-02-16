# Rekomendasi Channel untuk Dipantau

Sistem ini didesain untuk mendeteksi **harga** dan **nama barang/jasa**. Oleh karena itu, script ini akan bekerja paling maksimal di channel-channel berikut:

## 1. Forum Jual Beli (FJB) / Marketplace
Channel tempat orang memposting barang dagangan dengan format jelas.
*   **Contoh Nama/Keyword**: "FJB Indonesia", "Marketplace Indo", "Jual Beli Gadget", "Lapak Gaming".
*   **Kenapa Cocok?**: Postingan biasanya berisi format standar seperti "Dijual...", "Harga: Rp...", "Kondisi...". Regex kita sangat akurat di sini.
*   **Contoh Barang**: HP Bekas, Akun Game, Laptop, Sepatu.

## 2. Freelance & Job Boards
Channel lowongan kerja freelance, terutama yang mencantumkan *budget*.
*   **Contoh Nama/Keyword**: "Freelance Jobs", "Hiring Devs", "Remote Work Indonesia".
*   **Kenapa Cocok?**: Sering ada tulisan "Budget: 00" atau "Fee: Rp 1.000.000". Script akan menangkap ini sebagai "Harga".

## 3. P2P Crypto & Exchanger
Channel jual beli saldo crypto atau digital currency secara perorangan.
*   **Contoh Nama/Keyword**: "Jual Beli Saldo Paypal", "P2P Binance", "WTS USDT".
*   **Kenapa Cocok?**: Formatnya sangat kaku, misal "WTS 100 USDT Rate 15000". Script bisa menangkap angka dan mata uangnya dengan mudah.

## 4. Promo & Diskon
Channel yang membagikan info diskon.
*   **Contoh Nama/Keyword**: "Info Diskon", "Racun Shopee", "Promo Tiket".
*   **Kenapa Cocok?**: Bot bisa melacak perubahan harga atau harga promo yang diposting admin.

---

## Cara Mencari Channel Tersebut

Gunakan fitur pencarian (Search) di aplikasi Telegram dengan kata kunci:
1.  `@fjb...`
2.  `@market...`
3.  `@jualbeli...`
4.  `@freelance...`

Atau cari di website direktori Telegram seperti [Telegram Channels](https://tgstat.com/).

## Format Pesan yang Paling Bagus Terdeteksi

Script ini paling suka format seperti ini:

> **Jual iPhone 11**  (Baris pertama jadi Nama Barang)
> Kondisi Mulus
> **Harga: Rp 4.500.000** (Ada kata kunci "Harga:" atau "Price:")
> Lokasi Jakarta

Jika channel isinya cuma ngobrol (chatting) tanpa angka harga, script ini tidak akan berguna.
