try:
    import tkinter as tk #python3
except ImportError:
    import Tkinter as tk #python2

def generate_new_window():
    window = tk.Toplevel()
    label = tk.Label(window, text="a generic Toplevel window")
    label.pack()

root = tk.Tk()

spawn_window_button = tk.Button(root,
                                text="make a new window!",
                                command=generate_new_window)
spawn_window_button.pack()

root.mainloop()