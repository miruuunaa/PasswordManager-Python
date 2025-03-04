import tkinter as tk
from tkinter import messagebox
from file_storage import save_password
import random
import string

def generate_password():
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(12))

def create_window():
    window = tk.Tk()
    window.title("Password Manager")
    window.geometry("400x300")
    window.config(bg="#f4f4f4")

    tk.Label(window, text="Service:").pack(pady=5)
    service_entry = tk.Entry(window)
    service_entry.pack(pady=5)

    tk.Label(window, text="Username:").pack(pady=5)
    username_entry = tk.Entry(window)
    username_entry.pack(pady=5)

    tk.Label(window, text="Password:").pack(pady=5)
    password_entry = tk.Entry(window)
    password_entry.pack(pady=5)

    def save():
        service = service_entry.get()
        username = username_entry.get()
        password = password_entry.get()
        if service and username and password:
            save_password(service, username, password)
            messagebox.showinfo("Succes", "Parola a fost salvată cu succes!")
        else:
            messagebox.showwarning("Eroare", "Completează toate câmpurile!")

    def generate():
        password_entry.delete(0, tk.END)
        password_entry.insert(0, generate_password())

    tk.Button(window, text="Save Password", command=save, bg="#4caf50", fg="white").pack(pady=10)
    tk.Button(window, text="Generate Password", command=generate, bg="#2196f3", fg="white").pack(pady=5)

    window.mainloop()

if __name__ == "__main__":
    create_window()
