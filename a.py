import tkinter as tk
from tkinter import messagebox

# Laptoplar bazasi
laptops = {
    "Dell Inspiron 15": {
        "CPU": "Intel Core i5 11th Gen",
        "RAM": "8 GB",
        "SSD": "512 GB",
        "Price": "$650"
    },
    "HP Pavilion": {
        "CPU": "Intel Core i7 12th Gen",
        "RAM": "16 GB",
        "SSD": "1 TB",
        "Price": "$950"
    },
    "Lenovo IdeaPad": {
        "CPU": "AMD Ryzen 5",
        "RAM": "8 GB",
        "SSD": "256 GB",
        "Price": "$500"
    },
    "MacBook Air M2": {
        "CPU": "Apple M2",
        "RAM": "8 GB",
        "SSD": "256 GB",
        "Price": "$450"
    }
}

def search_laptop():
    name = entry.get()

    if name in laptops:
        data = laptops[name]
        info = f"""
🖥 Laptop: {name}

⚙ CPU: {data['CPU']}
🧠 RAM: {data['RAM']}
💾 SSD: {data['SSD']}
💰 Price: {data['Price']}
"""
        messagebox.showinfo("Laptop Info", info)
    else:
        messagebox.showerror("Xato", "Bunday laptop topilmadi ❌")

# UI
root = tk.Tk()
root.title("💻 Laptop Search")
root.geometry("420x300")
root.config(bg="#1e1e2f")

title = tk.Label(root, text="Laptop Qidirish",
                 font=("Arial", 18, "bold"),
                 fg="white", bg="#1e1e2f")
title.pack(pady=10)

label = tk.Label(root, text="Laptop nomini kiriting:",
                 font=("Arial", 12),
                 fg="lightgray", bg="#1e1e2f")
label.pack(pady=5)

# Input field
entry = tk.Entry(root, font=("Arial", 12), width=30)
entry.pack(pady=5)

# Search button
search_btn = tk.Button(root,
                       text="Qidirish 🔍",
                       font=("Arial", 12, "bold"),
                       bg="#4CAF50",
                       fg="white",
                       command=search_laptop)
search_btn.pack(pady=10)

# Exit button
exit_btn = tk.Button(root,
                     text="Chiqish",
                     font=("Arial", 12, "bold"),
                     bg="red",
                     fg="white",
                     command=root.quit)
exit_btn.pack(pady=10)

root.mainloop()