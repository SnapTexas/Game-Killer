import tkinter as tk
import time
from PIL import Image, ImageTk


app = tk.Tk()
app.withdraw()   # hide the main window


def render_gif(filename, time_play):
    root = tk.Toplevel()

    # Window size
    window_width = 300
    window_height = 300

    # Center window on screen
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2

    root.geometry(f"{window_width}x{window_height}+{x}+{y}")

    # Window settings
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    # Label for GIF
    label = tk.Label(root)
    label.pack()

    # Load GIF frames
    frames = []

    gif = Image.open(f"memes\\{filename}")

    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))
    except EOFError:
        pass

    # Start timer
    start_time = time.time()

    def play_frame(index):
        elapsed_time = time.time() - start_time

        # Stop after time_play seconds
        if elapsed_time >= time_play:
            root.destroy()
            return

        label.config(image=frames[index])

        # Loop GIF
        next_index = (index + 1) % len(frames)

        root.after(
            50,
            lambda: play_frame(next_index)
        )

    play_frame(0)


def main():
    render_gif("m1.gif", 10)

    app.mainloop()


if __name__ == "__main__":
    main()