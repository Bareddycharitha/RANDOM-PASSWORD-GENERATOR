
import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showwarning("Warning", "Password length must be at least 4")
            return
        
        characters = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(characters) for _ in range(length))

        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

def copy_password():
    password = result_entry.get()
    if password:
        window.clipboard_clear()
        window.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")

window = tk.Tk()
window.title("Random Password Generator")
window.geometry("400x250")
window.config(bg="#f0f0f0")

title_label = tk.Label(window, text="🔐 Random Password Generator", font=("Arial", 14, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

length_label = tk.Label(window, text="Enter password length:", font=("Arial", 12), bg="#f0f0f0")
length_label.pack()

length_entry = tk.Entry(window, font=("Arial", 12), justify="center")
length_entry.pack(pady=5)

generate_btn = tk.Button(window, text="Generate Password", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=generate_password)
generate_btn.pack(pady=10)

result_entry = tk.Entry(window, font=("Arial", 12), width=30, justify="center")
result_entry.pack(pady=5)

copy_btn = tk.Button(window, text="Copy to Clipboard", font=("Arial", 12), bg="#2196F3", fg="white", command=copy_password)
copy_btn.pack(pady=10)

window.mainloop()


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(',')', '*', '+' ]

no_lettters= int(input("How many letters in your password:"))
no_numbers= int(input("How many numbers in your password:"))
no_symbols= int(input("How many symbols in your password:"))

password_list =[]

for i in range(1,no_lettters+1):
    char = random.choice(letters)
    password_list += char

for i in range(1,no_numbers+1):
    char = random.choice(numbers)
    password_list += char

for i in range(1,no_symbols+1):
    char = random.choice(symbols)
    password_list += char


random.shuffle(password_list)

password=""
for char in password_list:
   password += char

print(password)
