import tkinter as tk
from PIL import Image, ImageTk


app = tk.Tk()
app.withdraw()   # hide the main window


def render_gif(filename):
    root = tk.Toplevel()

    root.geometry("300x300+500+300")
    root.overrideredirect(True)
    root.attributes("-topmost", True)

    label = tk.Label(root)
    label.pack()

    frames = []

    gif = Image.open(f"memes\\{filename}")

    try:
        while True:
            frames.append(ImageTk.PhotoImage(gif.copy()))
            gif.seek(len(frames))
    except EOFError:
        pass

    def play_frame(index):
        if index < len(frames):
            label.config(image=frames[index])
            root.after(50, lambda: play_frame(index + 1))
        else:
            root.destroy()

    play_frame(0)

def main():
    render_gif("m1.gif")
    
    app.mainloop()
if __name__=='__main__':
    main()
    