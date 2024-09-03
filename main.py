import tkinter as tk
from tkinter import messagebox, filedialog
import yt_dlp
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3
import warnings
warnings.filterwarnings('ignore')


def download_audio(url, save_path):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            title = info_dict.get('title', None)
            if title:
                tag_metadata(f"{save_path}/{title}.mp3", info_dict)
        messagebox.showinfo("Success", "Audio download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def download_video(url, save_path):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': f'{save_path}/%(title)s.%(ext)s',
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        messagebox.showinfo("Success", "Video download complete!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def tag_metadata(filepath, info_dict):
    try:
        audio = MP3(filepath, ID3=EasyID3)
        audio['title'] = info_dict.get('title', 'Unknown')
        audio['artist'] = info_dict.get('uploader', 'Unknown')
        audio.save()
    except Exception as e:
        messagebox.showerror("Error", f"Failed to tag metadata: {e}")


def start_download():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a URL.")
        return

    save_path = filedialog.askdirectory()
    if not save_path:
        messagebox.showerror("Error", "Please select a save directory.")
        return

    download_type = download_type_var.get()
    if download_type == 'audio':
        download_audio(url, save_path)
    elif download_type == 'video':
        download_video(url, save_path)
    else:
        messagebox.showerror("Error", "Invalid download type selected.")


# GUI setup
root = tk.Tk()
root.title("Media Downloader")

tk.Label(root, text="Enter the URL of the video:").grid(row=0, column=0, padx=10, pady=10)
url_entry = tk.Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Select download type:").grid(row=1, column=0, padx=10, pady=10)
download_type_var = tk.StringVar(value="audio")
tk.Radiobutton(root, text="Audio", variable=download_type_var, value="audio").grid(row=1, column=1, sticky="w")
tk.Radiobutton(root, text="Video", variable=download_type_var, value="video").grid(row=1, column=1, sticky="e")

download_button = tk.Button(root, text="Download", command=start_download)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
