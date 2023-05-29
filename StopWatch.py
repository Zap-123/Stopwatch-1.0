# Imports
import tkinter as tk
import time
import math

# Create Window
root = tk.Tk()
root.title("Timer") 
root.configure(bg="black")
root.geometry("210x125")
root.wm_attributes("-topmost", True)
root.resizable(width=False, height=False)

# Define Variables
is_running = False
start_time = 0.0
elapsed_time = 0.0

# Create the display
display_var = tk.StringVar()
display_label = tk.Label(root, textvariable=display_var, font=("Arial", 26), width=10, fg="white", bg="black")
display_label.pack(pady=20)


def start_pause():
    global is_running, start_time, elapsed_time

    # Start / Pause toggle & functionality
    if not is_running:
        is_running = True
        button.config(text="Pause")
        if elapsed_time == 0.0:
            start_time = time.time()
        else:
            start_time = time.time() - elapsed_time
    else:
        is_running = False
        button.config(text="Start")
        elapsed_time = time.time() - start_time


def reset():
    # Reset variables and display
    global is_running, start_time, elapsed_time
    is_running = False
    button.config(text="Start")
    start_time = 0.0
    elapsed_time = 0.0


def update_time():
    global is_running, elapsed_time

    # Loops logic & display
    if is_running:
        elapsed_time = time.time() - start_time

    minutes, seconds = divmod(int(elapsed_time), 60)
    hours, minutes = divmod(minutes, 60)
    milliseconds = math.floor((int((elapsed_time - int(elapsed_time)) * 1000) / 10))

    time_str = "{:02d}:{:02d}:{:02d}.{:02d}".format(hours, minutes, seconds, milliseconds)
    display_var.set(time_str)

    root.after(40, update_time)


# Creates GUI
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=5)

button = tk.Button(button_frame, text="Start", width=12, command=start_pause, fg="white", bg="black")
button.pack(side=tk.LEFT, padx=2)

reset_button = tk.Button(button_frame, text="Reset", width=12, command=reset, fg="white", bg="black")
reset_button.pack(side=tk.LEFT, padx=2)

update_time()

root.mainloop()
