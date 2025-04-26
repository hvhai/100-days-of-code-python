import tkinter as tk  # Use this import style for clarity

root = tk.Tk()
root.title("Coffee Machine")
root.geometry("300x100")  # Set window size

label = tk.Label(root, text="Coffee Machine")
label.grid(row=0, column=0)

root.mainloop()