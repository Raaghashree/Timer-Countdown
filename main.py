import time
import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Progressbar


def countdown(t, progress_bar, root, total_time):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        label.config(text=timer)
        progress = (t / total_time) * 100
        progress_bar['value'] = progress
        root.update_idletasks()
        time.sleep(1)
        t -= 1

    label.config(text="00:00")
    messagebox.showinfo("Time's up", "Countdown is over!")


root = tk.Tk()
root.title("Countdown Timer")
root.geometry("300x300")
root.config(bg="#2e3d49")

title_label = tk.Label(root, text="Countdown Timer", font=("Arial", 24, "bold"), fg="#FFFFFF", bg="#2e3d49")
title_label.pack(pady=20)

label = tk.Label(root, font=("Arial", 40), fg="#ff4747", bg="#2e3d49")
label.pack(pady=20)

entry_label = tk.Label(root, text="Enter time in seconds:", font=("Arial", 14), fg="#FFFFFF", bg="#2e3d49")
entry_label.pack()

time_entry = tk.Entry(root, font=("Arial", 14), width=10)
time_entry.pack(pady=10)


def start_countdown():
    try:
        total_time = int(time_entry.get())
        progress_bar['value'] = 0
        countdown(total_time, progress_bar, root, total_time)
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")


start_button = tk.Button(root, text="Start Countdown", font=("Arial", 14, "bold"), bg="#4CAF50", fg="white",
                         command=start_countdown, relief="raised", bd=5)
start_button.pack(pady=20)

progress_bar = Progressbar(root, length=300, mode='determinate', maximum=100)
progress_bar.pack(pady=10)

root.mainloop()
