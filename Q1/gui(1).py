# gui.py

import tkinter as tk
from tkinter import filedialog, messagebox
# Import the encryption functions from the separate encryption module
from encryption import encrypt_text, decrypt_text, verify_decryption

def process_files():
    """
    Main function that handles the complete encryption/decryption workflow.
    Reads user inputs, processes the text file, and saves results to new files.
    """
    # Get shift values from GUI entry fields and validate they are integers
    try:
        shift1 = int(shift1_entry.get())
        shift2 = int(shift2_entry.get())
    except ValueError:
        # Show error message if user entered non-integer values
        messagebox.showerror("Input Error", "Please enter valid integer values for both shifts.")
        return

    # Read the input file containing the text to encrypt
    try:
        with open('raw_text.txt', "r") as file:
            raw_text = file.read()
    except FileNotFoundError:
        # Show error message if the required input file doesn't exist
        messagebox.showerror("File Error", "raw_text.txt not found.")
        return

    # Encrypt the text using the provided shift values
    encrypted_text = encrypt_text(raw_text, shift1, shift2)
    # Save the encrypted text to a new file
    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted_text)

    # Decrypt the encrypted text to verify the process works correctly
    decrypted_text = decrypt_text(encrypted_text, shift1, shift2)
    # Save the decrypted text to a new file
    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted_text)

    # Verify that the decryption worked by comparing with original text
    if verify_decryption(raw_text, decrypted_text):
        messagebox.showinfo("Success", "Decryption verified successfully.")
    else:
        messagebox.showerror("Verification Failed", "Decryption did not match the original text.")

# GUI Setup
# Create the main application window
root = tk.Tk()
root.title("Text File Encryption and Decryption")

# Create and pack the first shift input field with label
tk.Label(root, text="Shift 1:").pack(padx=10, pady=5)
shift1_entry = tk.Entry(root)
shift1_entry.pack(padx=10, pady=5)

# Create and pack the second shift input field with label
# Note: Currently shift2 is not used in the encryption logic but kept for future functionality
tk.Label(root, text="Shift 2:").pack(padx=10, pady=5)
shift2_entry = tk.Entry(root)
shift2_entry.pack(padx=10, pady=5)

# Create and pack the process button that triggers the encryption/decryption workflow
process_button = tk.Button(root, text="Process", command=process_files)
process_button.pack(padx=10, pady=20)

# Start the GUI event loop - keeps the window open and responsive to user interactions
root.mainloop()