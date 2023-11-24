from pytube import YouTube, Playlist
import tkinter as tk
from tkinter import filedialog

def download_video():
    video_link = video_entry.get()
    output_video = filedialog.askdirectory()
    quality = quality_var.get()
    video = YouTube(video_link)

    # Check if the requested quality is available
    video_stream = video.streams.filter(res=quality).first()
    if video_stream:
        video_stream.download(output_path=output_video)
        download_complete_label.config(text="Download Done")
    else:
        download_complete_label.config(text="Selected quality not available for the video")

def download_playlist():
    playlist_link = playlist_entry.get()
    output_playlist = filedialog.askdirectory()
    quality = quality_var.get()
    playlist = Playlist(playlist_link)

    for video in playlist.videos:
        # Check if the requested quality is available for each video in the playlist
        video_stream = video.streams.filter(res=quality).first()
        if video_stream:
            video_stream.download(output_path=output_playlist)

    download_complete_label.config(text="Download Done")

# Create the main window
window = tk.Tk()
window.title("YouTube Downloader")

# Video Download Section
video_label = tk.Label(window, text="Video URL:")
video_label.grid(row=0, column=0, padx=10, pady=10)
video_entry = tk.Entry(window, width=40)
video_entry.grid(row=0, column=1, padx=10, pady=10)

# Quality Selection for Video
quality_label = tk.Label(window, text="Select Quality:")
quality_label.grid(row=0, column=2, padx=10, pady=10)
qualities = ["144p", "240p", "360p", "480p", "720p"]
quality_var = tk.StringVar(window)
quality_var.set(qualities[0])  # Default quality selection
quality_menu = tk.OptionMenu(window, quality_var, *qualities)
quality_menu.grid(row=0, column=3, padx=10, pady=10)

video_button = tk.Button(window, text="Download Video", command=download_video)
video_button.grid(row=0, column=4, padx=10, pady=10)

# Playlist Download Section
playlist_label = tk.Label(window, text="Playlist URL:")
playlist_label.grid(row=1, column=0, padx=10, pady=10)
playlist_entry = tk.Entry(window, width=40)
playlist_entry.grid(row=1, column=1, padx=10, pady=10)

# Quality Selection for Playlist
quality_label = tk.Label(window, text="Select Quality:")
quality_label.grid(row=1, column=2, padx=10, pady=10)
quality_menu = tk.OptionMenu(window, quality_var, *qualities)
quality_menu.grid(row=1, column=3, padx=10, pady=10)

playlist_button = tk.Button(window, text="Download Playlist", command=download_playlist)
playlist_button.grid(row=1, column=4, padx=10, pady=10)

# Download Complete Label
download_complete_label = tk.Label(window, text="")
download_complete_label.grid(row=2, column=0, columnspan=5, pady=10)

# Run the main loop
window.mainloop()
