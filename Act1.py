import tkinter as tk

# Data
compostable = [
    "banana peel", "apple core", "orange peel", "egg shells",
    "coffee grounds", "tea bags", "vegetable scraps",
    "paper towel", "leaves", "grass"
]

not_compostable = [
    "plastic", "glass", "metal", "styrofoam",
    "plastic bag", "rubber", "aluminum foil","cardboard"
]

def check_item():
    item = entry.get().lower()

    if item in compostable:
        result_label.config(text="✅ Compostable!", fg="#2ecc71")
    elif item in not_compostable:
        result_label.config(text="❌ Not Compostable", fg="#e74c3c")
    else:
        result_label.config(text="⚠️ Item not in database", fg="#f39c12")

# Window
root = tk.Tk()
root.title("Compost Checking App")
root.geometry("300x300")
root.configure(bg="#e8f5e9")

# Title
title = tk.Label(
    root,
    text="🌱 Compost Checker",
    font=("Helvetica", 22, "bold"),
    bg="#e8f5e9",
    fg="#2c3e50"
)
title.pack(pady=20)

label = tk.Label(root, 
                 text="Please enter the material you are composting!",
                 font=("Helvetica",10),
                 bg="#e8f5e9",
                 fg="#2c3e50"
)
label.pack(pady=10)
# Input box
entry = tk.Entry(
    root,
    font=("Helvetica", 14),
    width=25,
    justify="center"
)
entry.pack(pady=10)

# Button
check_button = tk.Button(
    root,
    text="Check Item",
    font=("Helvetica", 12, "bold"),
    bg="#27ae60",
    fg="white",
    padx=20,
    pady=5,
    command=check_item
)
check_button.pack(pady=10)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Helvetica", 16),
    bg="#e8f5e9"
)
result_label.pack(pady=20)

root.mainloop()