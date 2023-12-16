import tkinter as tk
from tkinter import filedialog, simpledialog

class PlaylistWindow:
    def __init__(self, master, playlist):
        self.master = master
        self.master.title("BeatSync - Playlist Window")
        self.master.geometry("400x300")
        self.master.configure(bg='#4169E1')  # Set background color to royal blue

        self.playlist = playlist

        # Widgets
        self.label = tk.Label(master, text="Playlist", font=("Helvetica", 16), bg='#4169E1', fg='white')
        self.label.pack(pady=10)

        self.show_button = tk.Button(master, text="Show Playlist", command=self.show_playlist, bg='#87CEFA')
        self.show_button.pack(pady=10)

    def show_playlist(self):
        if not self.playlist:
            print("Playlist is empty.")
        else:
            print("Current Playlist:")
            for i, song in enumerate(self.playlist, start=1):
                print(f"{i}. {song}")


class BeatSyncApp:
    def __init__(self, root):
        self.root = root
        self.root.title("BeatSync - Music Playlist App")
        self.root.geometry("400x300")
        self.root.configure(bg='#4169E1')  # Set background color to royal blue

        self.playlist = []

        # Password protection
        self.password_protected = False
        self.password = "your_password"  # Replace with your desired password

        # Widgets
        self.label = tk.Label(root, text="BeatSync - Music Playlist App", font=("Helvetica", 16), bg='#4169E1', fg='white')
        self.label.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Song", command=self.add_song, bg='#87CEFA')
        self.add_button.pack(pady=10)

        self.show_button = tk.Button(root, text="Show Playlist", command=self.show_playlist, bg='#87CEFA')
        self.show_button.pack(pady=10)

        self.password_button = tk.Button(root, text="Toggle Password Protection", command=self.toggle_password, bg='#87CEFA')
        self.password_button.pack(pady=10)

        self.playlist_window_button = tk.Button(root, text="Open Playlist Window", command=self.open_playlist_window, bg='#87CEFA')
        self.playlist_window_button.pack(pady=10)

    def add_song(self):
        file_path = filedialog.askopenfilename(title="Select a song", filetypes=[("MP3 files", "*.mp3")])
        if file_path:
            self.playlist.append(file_path)
            print(f"Added '{file_path}' to the playlist.")

    def show_playlist(self):
        if self.password_protected:
            password = simpledialog.askstring("Password", "Enter your password:", show='*')
            if password != self.password:
                print("Incorrect password. Access denied.")
                return

        if not self.playlist:
            print("Playlist is empty.")
        else:
            print("Current Playlist:")
            for i, song in enumerate(self.playlist, start=1):
                print(f"{i}. {song}")

    def toggle_password(self):
        self.password_protected = not self.password_protected
        status = "enabled" if self.password_protected else "disabled"
        print(f"Password protection {status}.")

    def open_playlist_window(self):
        playlist_window = tk.Toplevel(self.root)
        PlaylistWindow(playlist_window, self.playlist)


if __name__ == "__main__":
    root = tk.Tk()
    app = BeatSyncApp(root)
    root.mainloop()
