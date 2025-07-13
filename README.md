
### 🔐 Password Generator – Python Project

This project is a simple yet effective **random password generator** written in Python. It helps users generate **strong, secure passwords** by combining lowercase letters, numbers, and special symbols. Strong passwords are essential for protecting online accounts from being hacked, and this program makes it easy to create one instantly.

### 💡 How It Works

The program begins by importing Python's built-in `random` module to allow random selection of characters. It defines three separate lists:

* **Letters:** All lowercase alphabets (`a` to `z`)
* **Numbers:** Digits from `1` to `9`
* **Symbols:** A wide range of special characters like `@`, `#`, `!`, `&`, etc.

A list of 10 placeholders is used to store characters for the password. Then, using a `for` loop that runs 10 times, the program randomly decides whether to add a letter, number, or symbol in each position. It selects one character from the chosen list and inserts it into the password.

After the loop completes, the list of characters is joined into a single string using `join()`, and the final password is printed.

### ✅ Features

* Generates random 10-character passwords
* Mixes letters, numbers, and symbols for strong security
* Lightweight and easy to understand
* Fully written in basic Python — no external packages required

### 🛠️ Requirements

* Python 3.x
* No additional libraries needed

### 📌 How to Use

1. Download or clone the repository.
2. Open the file in any Python IDE or text editor.
3. Run the script.
4. A new password will be displayed in the terminal.

