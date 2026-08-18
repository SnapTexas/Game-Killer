import tkinter as tk
from PIL import Image, ImageTk
import time


def render_gif(filename, time_play):

    root = tk.Tk()

    window_width = 300
    window_height = 300

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    root.overrideredirect(True)
    root.attributes("-topmost", True)

    label = tk.Label(root)
    label.pack()

    frames = []

    gif = Image.open(rf"memes\{filename}")

    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))
    except EOFError:
        pass

    start_time = time.time()

    def play_frame(index):

        if time.time() - start_time >= time_play:
            root.destroy()
            return

        label.config(image=frames[index])

        next_index = (index + 1) % len(frames)

        root.after(
            50,
            lambda: play_frame(next_index)
        )

    play_frame(0)

    root.mainloop()