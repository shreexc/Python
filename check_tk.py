import tkinter as tk

root = tk.Tk()
root.title("Tkinter Installation")
root.geometry("700x300")

label = tk.Label(root, text="Congratulations, Tkinter is installed.", font=("Sans-Serif", 15))
label.pack(expand=True)
root.mainloop()
