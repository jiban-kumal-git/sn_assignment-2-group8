# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
from encryption import encrypt_text, decrypt_text, verify_decryption

def process_files():
    try:
        shift1 = int(shift1_entry.get())
        shift2 = int(shift2_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid integer values for both shifts.")
        return

    try:
        with open('raw_text.txt', "r") as file:
            raw_text = file.read()
    except FileNotFoundError:
        messagebox.showerror("File Error", "raw_text.txt not found.")
        return

    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

    if verify_decryption(raw_text, decrypted_text):
        messagebox.showinfo("Success", "Decryption verified successfully.")
    else:
        messagebox.showerror("Verification Failed", "Decryption did not match the original text.")

# GUI Setup
root = tk.Tk()
root.title("Text File Encryption and Decryption")

tk.Label(root, text="Shift 1:").pack(padx=10, pady=5)
shift1_entry = tk.Entry(root)
shift1_entry.pack(padx=10, pady=5)

tk.Label(root, text="Shift 2:").pack(padx=10, pady=5)
shift2_entry = tk.Entry(root)
shift2_entry.pack(padx=10, pady=5)

process_button = tk.Button(root, text="Process", command=process_files)
process_button.pack(padx=10, pady=20)

root.mainloop()
