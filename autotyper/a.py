import tkinter as tk
import pyautogui
import time
import threading

def start_typing():
    text = text_entry.get("1.0", tk.END).strip()
    delay = float(delay_entry.get())
    
    time.sleep(3)  # Small delay to switch to the input field
    for char in text:
        pyautogui.typewrite(char)
        time.sleep(delay)

def start_thread():
    thread = threading.Thread(target=start_typing)
    thread.daemon = True
    thread.start()

# Create the main window
root = tk.Tk()
root.title("AutoTyper")
root.geometry("400x300")

# Add input fields
text_label = tk.Label(root, text="Enter text to type:")
text_label.pack()

text_entry = tk.Text(root, height=5, width=40)
text_entry.pack()

delay_label = tk.Label(root, text="Typing speed (seconds per character):")
delay_label.pack()

delay_entry = tk.Entry(root)
delay_entry.insert(0, "0.1")  # Default delay value
delay_entry.pack()

# Start button
start_button = tk.Button(root, text="Start Typing", command=start_thread)
start_button.pack()

# Run the Tkinter loop
root.mainloop()
