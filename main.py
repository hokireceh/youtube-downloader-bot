from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackContext, filters
from yt_dlp import YoutubeDL
import os
from dotenv import load_dotenv

# Load token dari .env
load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

# Membaca proxy dari proxy.txt
def get_proxy():
    with open('proxy.txt', 'r') as file:
        return file.read().strip()

# Direktori untuk menyimpan file sementara
DOWNLOAD_DIR = "downloads"
os.makedirs(DOWNLOAD_DIR, exist_ok=True)

async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(
        "Halo! Kirimkan link video YouTube, dan saya akan mendownloadnya dengan resolusi terbaik untuk Anda. 😊"
    )

async def download_video(update: Update, context: CallbackContext) -> None:
    url = update.message.text

    if "youtube.com" not in url and "youtu.be" not in url:
        await update.message.reply_text("URL tidak valid. Pastikan itu adalah link YouTube.")
        return

    await update.message.reply_text("Sedang memproses video... Mohon tunggu sebentar.")

    try:
        proxy = get_proxy()  # Ambil proxy dari file

        ydl_opts = {
            'format': 'bestaudio[ext=m4a]+bestvideo[ext=mp4]/best',  # Memilih format audio dan video yang lebih kompatibel
            'merge_output_format': 'mp4',  # Gabungkan video dan audio ke MP4
            'outtmpl': f'{DOWNLOAD_DIR}/%(title)s.%(ext)s',  # Tempat penyimpanan
            'proxy': proxy,  # Gunakan proxy dari file
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4',  # Menggunakan format MP4 untuk penggabungan
            }],
            'headers': {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
            },
        }

        with YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)

        with open(file_path, 'rb') as video:
            await update.message.reply_video(video)  # Kirim video ke pengguna tanpa 'timeout'
        
        # Hapus file setelah dikirim
        if file_path.endswith('.mp4'):  # Cek apakah file yang dikirim adalah file video
            os.remove(file_path)


    except Exception as e:
        await update.message.reply_text(f"Terjadi kesalahan: {str(e)}")

def main():
    # Inisialisasi bot dengan token dari .env
    application = Application.builder().token(API_TOKEN).build()

    # Command handlers
    application.add_handler(CommandHandler("start", start))

    # Message handler untuk menerima URL
    application.add_handler(MessageHandler(filters.TEXT, download_video))  # Gunakan filters.TEXT (huruf kapital)

    # Jalankan bot
    application.run_polling()

if __name__ == '__main__':
    main()
