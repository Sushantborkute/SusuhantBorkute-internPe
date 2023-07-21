import tkinter as tk
import time
from datetime import date

def clock():
    current_time = time.strftime("%H:%M:%S %p")
    current_date = date.today().strftime("%B %d, %Y")
    current_day = date.today().strftime("%A")
    clock_label.config(text=current_time)
    date_label.config(text=current_date)
    day_label.config(text=current_day)
    clock_label.after(1000, clock)

window = tk.Tk()
window.title("Digital Clock")
window.geometry("300x150")
window.resizable(False, False)
window.configure(bg="black")

clock_label = tk.Label(window, font=("ds-digital", 40), fg="cyan", bg="black")
clock_label.pack(pady=5)

date_label = tk.Label(window, font=("ds-digital", 20), fg="cyan", bg="black")
date_label.pack()

day_label = tk.Label(window, font=("ds-digital", 20), fg="cyan", bg="black")
day_label.pack()

clock()
window.mainloop()
