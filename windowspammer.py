import math
import tkinter as tk
import random


class MainWindow(tk.Frame):
    counter = 0

    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        for y in range(16):
            for x in range(30):
                if x == y == 0:
                    continue
                self.create_window(x * 61, y * 63)

    def create_window(self, pos_x, pos_y):
        self.counter += 1
        t = tk.Toplevel(self)
        t.attributes('-toolwindow', True)
        t.wm_geometry("+%d+%d" % (pos_x, pos_y))
        t.wm_title(str(self.counter))
        l = tk.Label(t, text="Window")
        l.pack(side="top", fill="both", expand=True, padx=5, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    root.attributes('-toolwindow', True)
    root.wm_geometry("+%d+%d" % (0, 0))
    root.wm_title("0")
    l = tk.Label(root, text="Window")
    l.pack(side="top", fill="both", expand=True, padx=5, pady=5)
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
