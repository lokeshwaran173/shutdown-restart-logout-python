import os
import tkinter as tk
from tkinter import ttk

# Initialize the main window
main_window = tk.Tk()
main_window.geometry("400x300")
main_window.title("Lokesh Code")  # Updated title

# Set background color for the main window
main_window.configure(bg='#f0f0f0')  # Light gray background color

# Create a frame with padding
content_frame = ttk.Frame(main_window, padding=20)
content_frame.pack(fill=tk.BOTH, expand=True)

# Add a header label
header_label = ttk.Label(content_frame, text="System Control Panel", font=('Calibri', 18, 'bold'))
header_label.pack(pady=20)

# Define functions for system control
def power_off():
    os.system("shutdown /s /t 0")

def reboot():
    os.system("shutdown /r /t 0")

def sign_out():
    os.system("shutdown /l /t 0")

# Create control buttons with a modern style and individual background colors
shutdown_button = tk.Button(content_frame, text='Shutdown', command=power_off, font=('Arial', 12), 
                            bg='#FF6347', fg='white', activebackground='#FF4500', activeforeground='white', 
                            width=15, height=2)
shutdown_button.pack(pady=10)

restart_button = tk.Button(content_frame, text='Restart', command=reboot, font=('Arial', 12), 
                            bg='#4682B4', fg='white', activebackground='#4169E1', activeforeground='white', 
                            width=15, height=2)
restart_button.pack(pady=10)

logout_button = tk.Button(content_frame, text='Logout', command=sign_out, font=('Arial', 12), 
                            bg='#32CD32', fg='white', activebackground='#228B22', activeforeground='white', 
                            width=15, height=2)
logout_button.pack(pady=10)

# Run the Tkinter event loop
main_window.mainloop()
