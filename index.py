import tkinter as tk
from tkinter import messagebox
import itertools
import string

# User database with passwords
USER_DATABASE = {
    "alice": "hAcK3",
    "bob": "qWert",
    "charlie": "aabbb",
    "david": "ZyXwV",
    "eve": "AbCdE"
}

# Dictionary file (list of common passwords)
DICTIONARY = ["password", "12345", "qwerty", "letmein", "admin", "welcome", "hAcK3", "qWert", "P@ssw", "ZyXwV", "AbCdE"]

# Function to perform dictionary attack
def dictionary_attack(target_password):
    for password in DICTIONARY:
        if password == target_password:
            return password
    return None

# Function to perform brute force attack
def brute_force_attack(target_password):
    chars = string.ascii_letters  # A-Z, a-z
    for password in itertools.product(chars, repeat=5):
        password = "".join(password)
        output_text.insert(tk.END, f"Trying: {password}\n")  # Show attempts in the GUI
        root.update()
        if password == target_password:
            return password
    return None

# Function to start attack process
def start_attack():
    output_text.delete(1.0, tk.END)
    username = user_var.get()
    
    if username not in USER_DATABASE:
        messagebox.showerror("Error", "Username not found in the database")
        return
    
    target_password = USER_DATABASE[username]
    output_text.insert(tk.END, f"Starting attack on {username}...\n")
    
    # Try dictionary attack first
    output_text.insert(tk.END, "Starting Dictionary Attack...\n")
    cracked_password = dictionary_attack(target_password)
    if cracked_password:
        output_text.insert(tk.END, f"Password cracked using Dictionary Attack: {cracked_password}\n")
        messagebox.showinfo("Success", f"Password cracked using Dictionary Attack: {cracked_password}")
        return
    
    # If dictionary attack fails, use brute force
    output_text.insert(tk.END, "Dictionary Attack failed. Starting Brute Force Attack...\n")
    cracked_password = brute_force_attack(target_password)
    if cracked_password:
        output_text.insert(tk.END, f"Password cracked using Brute Force: {cracked_password}\n")
        messagebox.showinfo("Success", f"Password cracked using Brute Force: {cracked_password}")
    else:
        messagebox.showerror("Failure", "Failed to crack the password")

# GUI setup
root = tk.Tk()
root.title("Password Cracker")
root.geometry("500x500")
root.configure(bg="#0F0F0F")  # Darker theme for more intensity

# Create a canvas for the skull logo
canvas = tk.Canvas(root, width=100, height=100, bg="#0F0F0F", highlightthickness=0)
canvas.pack(pady=5)

# Draw a more intense skull
canvas.create_oval(20, 20, 80, 80, fill="white", outline="red", width=3)  # Skull head
canvas.create_oval(30, 35, 45, 50, fill="black")  # Left eye
canvas.create_oval(55, 35, 70, 50, fill="black")  # Right eye
canvas.create_oval(45, 60, 55, 70, fill="black")  # Nose
canvas.create_line(35, 85, 65, 85, fill="red", width=3)  # Mouth
canvas.create_line(40, 85, 42, 90, fill="red", width=3)  # Teeth
canvas.create_line(48, 85, 50, 90, fill="red", width=3)
canvas.create_line(56, 85, 58, 90, fill="red", width=3)

# UI Elements
title_label = tk.Label(root, text="Password Cracker", font=("Arial", 16, "bold"), fg="red", bg="#0F0F0F")
title_label.pack(pady=5)

# Dropdown for selecting user
user_var = tk.StringVar(root)
user_var.set(list(USER_DATABASE.keys())[0])  # Default selection
user_label = tk.Label(root, text="Select a user:", font=("Arial", 12), fg="white", bg="#0F0F0F")
user_label.pack()
user_dropdown = tk.OptionMenu(root, user_var, *USER_DATABASE.keys())
user_dropdown.config(bg="#222222", fg="white")
user_dropdown.pack(pady=5)

attack_button = tk.Button(root, text="Start Attack", font=("Arial", 12, "bold"), bg="red", fg="white", command=start_attack)
attack_button.pack(pady=10)

output_text = tk.Text(root, height=15, width=50, font=("Arial", 10), bg="#222222", fg="white")
output_text.pack(pady=10)

# Run GUI
root.mainloop()
