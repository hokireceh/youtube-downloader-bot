# Telegram Video Downloader Bot

Bot Telegram ini memungkinkan pengguna untuk mengirimkan link YouTube, dan bot akan mendownload video dengan resolusi terbaik (termasuk audio) dan mengirimkan video ke pengguna.

## Fitur
- Mendukung link YouTube dan YouTube Shorts.
- Mengunduh video dengan kualitas terbaik (audio dan video digabungkan).
- Menggunakan proxy jika diperlukan.
- Menyediakan pengunduhan video dalam format MP4.

## Persyaratan
Pastikan Anda memiliki Python 3.8 atau lebih baru terpasang di sistem Anda.

## Instalasi

1. Clone repositori ini atau unduh file sumber.
2. Buat file `.env` di direktori utama proyek dan masukkan token bot Telegram Anda:

```
API_TOKEN=your_telegram_bot_api_token
```
3. Install dependensi dengan menjalankan perintah berikut:
```
pip install -r requirements.txt
```
4. Jika Anda ingin menggunakan proxy untuk mengunduh video, buat file proxy.txt yang berisi alamat proxy Anda. (Opsional)

## Menjalankan Bot
Untuk menjalankan bot, jalankan perintah berikut di terminal:

```
python3 main.py

```
