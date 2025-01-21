import os
import tkinter as tk
from tkinter import filedialog, messagebox

def process_image(path: str, key: int, mode: str) -> None:
    """Encrypt or decrypt an image file"""
    try:
        if mode == "e":
            print(f"Encrypting image at {path} with key {key}...")
        else:
            print(f"Decrypting image at {path} with key {key}...")

        # Open the image file in binary read/write mode
        with open(path, "rb+") as file:
            # Read the entire file into a bytearray
            image = bytearray(file.read())
            # XOR each byte with the key to encrypt/decrypt
            for i, value in enumerate(image):
                image[i] = value ^ key
            # Move the file pointer to the beginning of the file
            file.seek(0)
            # Write the modified bytearray back to the file
            file.write(image)

        if mode == "e":
            messagebox.showinfo("Success", "Encryption successful!")
        else:
            messagebox.showinfo("Success", "Decryption successful!")
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")

def select_file():
    # Open a file dialog to select an image file
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png;*.bmp;*.gif")])
    # Update the file entry with the selected file path
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path)

def start_process():
    path = file_entry.get()  # Get the file path from the entry
    key = int(key_entry.get())  # Get the key from the entry
    mode = mode_var.get()  # Get the selected mode (encrypt/decrypt)

    # Check if the file path is valid
    if os.path.exists(path) and os.path.isfile(path):
        # Check if the key is within the valid range (0-255)
        if 0 <= key <= 255:
            process_image(path, key, mode)
        else:
            messagebox.showerror("Error", "Invalid key. Please enter a key between 0 and 255.")
    else:
        messagebox.showerror("Error", "Invalid path. Please enter a valid file path.")

# Initialize the main application window
app = tk.Tk()
app.title("Image Encryption/Decryption Tool")

# Mode selection (Encrypt/Decrypt)
mode_var = tk.StringVar(value="e")
encrypt_radio = tk.Radiobutton(app, text="Encrypt", variable=mode_var, value="e")
decrypt_radio = tk.Radiobutton(app, text="Decrypt", variable=mode_var, value="d")
encrypt_radio.grid(row=0, column=0, padx=10, pady=10)
decrypt_radio.grid(row=0, column=1, padx=10, pady=10)

# File selection
file_label = tk.Label(app, text="Image file:")
file_label.grid(row=1, column=0, padx=10, pady=10)
file_entry = tk.Entry(app, width=40)
file_entry.grid(row=1, column=1, padx=10, pady=10)
file_button = tk.Button(app, text="Browse", command=select_file)
file_button.grid(row=1, column=2, padx=10, pady=10)

# Key entry
key_label = tk.Label(app, text="Key (0-255):")
key_label.grid(row=2, column=0, padx=10, pady=10)
key_entry = tk.Entry(app)
key_entry.grid(row=2, column=1, padx=10, pady=10)

# Start button
start_button = tk.Button(app, text="Start", command=start_process)
start_button.grid(row=3, columnspan=3, pady=20)

# Run the application
app.mainloop()
