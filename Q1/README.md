# Structure
Q1/
├── data/
│   └── raw_text.txt        # Sample plaintext input
└── src/
    ├── __init__.py         # Marks 'src' as a Python package
    ├── gui.py              # GUI application logic
    ├── encryption.py       # Encryption and decryption functions
    └── file_operations.py  # Utility functions for file handling

# Running the Application

1. Navigate to the `src` directory:
   cd Q1/src
   python gui.py

# DEPENDENCIES
tkinter for the GUI:
pip install tk


# COMPONENTS BREAKDOWNS:
1. gui.py

Purpose: Provides the graphical interface for user interaction.

Key Functions:

process_files(): Handles file reading, encryption, decryption, and saving outputs.

GUI elements: Entry fields for shift values, labels, and buttons for user interaction.

2. encryption.py

Purpose: Contains the core encryption and decryption logic.

Key Functions:

shift_char(c, shift): Shifts a character by a specified number of positions.

encrypt_text(text, shift1, shift2): Encrypts the input text using two shift values.

decrypt_text(text, shift1, shift2): Decrypts the input text using the corresponding shift values.

verify_decryption(original_text, decrypted_text): Verifies if the decrypted text matches the original.

3. file_operations.py

Purpose: Provides utility functions for file handling.

Key Functions:

read_file(file_path): Reads the content of a specified file.

write_file(file_path, content): Writes content to a specified file.

4. raw_text.txt

Purpose: Contains the original plaintext to be encrypted.

Content: A sample passage demonstrating the encryption and decryption process.

5. encrypted_text.txt

Purpose: Stores the encrypted version of raw_text.txt.

Content: The result of encrypting raw_text.txt using the specified shifts.

6. decrypted_text.txt

Purpose: Stores the decrypted version of encrypted_text.txt.

Content: The result of decrypting encrypted_text.txt back to its original form.

# SETUP AND EXECUTION
Prerequisites

Python 3.x

Tkinter (usually bundled with Python)

No additional libraries are required for this project.

Running the Application

Navigate to the Q1 directory in your terminal or command prompt.

Execute the following command to start the GUI application:

python gui.py


The GUI will prompt you to enter two shift values for the encryption.

Upon entering the values, the application will:

Read raw_text.txt.

Encrypt the content using the provided shifts.

Save the encrypted content to encrypted_text.txt.

Decrypt the encrypted content.

Save the decrypted content to decrypted_text.txt.

Display a message box indicating whether the decryption was successful.

# TESTING AND VARIFICATON

Input: raw_text.txt contains the sentence: "The quick brown fox jumps over the lazy dog."

Shifts: 3 and 5

Expected Output:

encrypted_text.txt should contain the encrypted version of the input text.

decrypted_text.txt should match the original raw_text.txt content.

# NOTES

The application uses a simple Caesar cipher for encryption and decryption.

The GUI is built using Python's Tkinter library.

Ensure that raw_text.txt is present in the same directory as the script before running the application.