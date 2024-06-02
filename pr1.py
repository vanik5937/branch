import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S %p')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")

time_label = tk.Label(root, font=('Helvetica', 48), background='black', foreground='white')
time_label.pack(anchor='center')

update_time()

root.mainloop()